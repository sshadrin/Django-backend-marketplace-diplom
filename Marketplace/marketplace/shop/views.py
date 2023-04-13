from cart.forms import CartAddProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import CategoryForm, ReviewForm
from .models import Category, Product, Review
from rest_framework.generics import GenericAPIView
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, ReviewPostSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListView(ListView):
    """Создаем функцию для отображения Категорий в шаблоне"""
    template_name = 'shop/category.html'
    context_object_name = "categoryes"
    queryset = Category.objects.filter(soft_delete=False)


class CategoryList(ListModelMixin, GenericAPIView):
    """Создание generic Api view класса для отображения данных модели Category в браузере в формате json"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', ]

    def get(self, request: HttpRequest):
        return self.list(request)


class CategoryDetailView(DetailView):
    """Создаем функцию для отображения деталей кокретной категории"""
    template_name = 'shop/category-details.html'
    model = Category
    form_class = CategoryForm
    context_object_name = "category"


class ProductListView(ListView):
    """Создаем функцию для отображения продуктов в определенной категории"""
    template_name = 'shop/products.html'
    context_object_name = "products"

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Product.objects.filter(category=category, soft_delete=False)


class ProductList(ListModelMixin, GenericAPIView):
    """Создание generic Api view класса для отображения данных модели Product в браузере в формате json"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', ]

    def get(self, request: HttpRequest):
        return self.list(request)


class ProductsDetailView(DetailView):
    """Создаем функцию для отображения деталей продуктов"""
    template_name = 'shop/products-details.html'
    model = Product
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super(ProductsDetailView, self).get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context


class PopularListView(ListView):
    """Создаем функцию для отображения популярных товаров"""
    template_name = 'shop/popular.html'
    context_object_name = "populars"
    queryset = Product.objects.filter(soft_delete=False)


class PromotionListView(ListView):
    """Создаем функцию для отображения товаров по акциям"""
    template_name = 'shop/promotion.html'
    context_object_name = "promotion"
    queryset = Product.objects.filter(soft_delete=False)


class ReviewCreateView(LoginRequiredMixin, CreateView):
    """Создаем функцию для создания отзывов о продуктах"""
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy("shop:category")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        product = Product.objects.get(pk=self.kwargs['pk'])
        self.object.products = product
        self.object.user.profile.save()
        self.object.save()
        return HttpResponseRedirect(self.success_url)


class ReviewListView(LoginRequiredMixin, ListView):
    """Создаем функцию для отображения отзывов"""
    template_name = 'shop/review.html'
    context_object_name = "review"
    queryset = Review.objects.filter(soft_delete=False)


class ReviewList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Создание generic Api view класса для отображения данных модели Review и работы с
    ними в браузере в формате json"""
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_ad', ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewSerializer
        if self.request.method == 'POST':
            return ReviewPostSerializer


    def get(self, request: HttpRequest):
        return self.list(request)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request: HttpRequest):
        return self.create(request)
