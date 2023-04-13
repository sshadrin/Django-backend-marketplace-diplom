from rest_framework import viewsets
from .models import Order, OrderItem


class OrderViewSet(viewsets.ModelViewSet):
    """Создание API представлений модели Order в django rest framework"""
    queryset = Order.objects.all()


class OrderItemViewSet(viewsets.ModelViewSet):
    """Создание API представлений модели OrderItem в django rest framework"""
    queryset = OrderItem.objects.all()