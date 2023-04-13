from rest_framework import serializers
from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    """Создание сериализатора для преображения данных модели Order в байтовые объекты
    для последующего отображения их в json формате"""
    class Meta:
        model = Order
        fields = ["email", "delivery_adress", "promocode", "created_ad", ]


class OrderItemSerializer(serializers.ModelSerializer):
    """Создание сериализатора для преображения данных модели OrderItem в байтовые объекты
    для последующего отображения их в json формате"""
    class Meta:
        model = OrderItem
        fields = ["order", "user", "products", "price", "quantity", "soft_delete", ]
