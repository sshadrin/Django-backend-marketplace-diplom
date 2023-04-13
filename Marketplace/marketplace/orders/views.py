from django.http import HttpRequest

from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.db import transaction

from .forms import OrdersForm
from .models import Order, OrderItem, Product

from rest_framework.generics import GenericAPIView
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from django_filters.rest_framework import DjangoFilterBackend


@login_required
@transaction.atomic
def order_create(request):
    """Функция обрабатывающая заказ. Списывает баланс у пользователя, убавляет кол-во товара на складе,
    прибавляет кол-во проданного товара"""
    cart = Cart(request)
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            user = request.user
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         user=user,
                                         products=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                price = Product.objects.get(pk=item['product'].pk)
                request.user.profile.balance -= (price.total_price) * item['quantity']
                price.sale_count += 1
                price.stock -= 1
                price.save()
                request.user.profile.save()
            cart.clear()
            return render(request, 'orders/create.html',
                          {'order': order})
    else:
        form = OrdersForm
    return render(request, 'orders/order_form.html',
                  {'cart': cart, 'form': form})


class OrderList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Создание generic Api view класса для отображения данных модели Order и работы с
    ними в браузере в формате json"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_fields = ['created_ad', ]

    def get(self, request: HttpRequest):
        return self.list(request)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request: HttpRequest):
        return self.create(request)


class OrderhistoryListView(LoginRequiredMixin, ListView):
    """Создаем функцию для отображения модели Истории заказов в шаблоне"""
    template_name = 'orders/order-history.html'
    context_object_name = "history"
    queryset = OrderItem.objects.filter(soft_delete=False)


class OrderhistoryList(ListModelMixin, GenericAPIView):
    """Создание generic Api view класса для отображения данных модели Order в браузере в формате json"""
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order', ]

    def get(self, request: HttpRequest):
        return self.list(request)


class OrdersDetailView(LoginRequiredMixin, DetailView):
    """Создаем функцию для отображения в шаблоне деталей заказа из истории заказов"""
    template_name = 'orders/orders-detail.html'
    model = Order
    form_class = OrdersForm
    context_object_name = "orders"
