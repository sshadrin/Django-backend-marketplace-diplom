from rest_framework import serializers
from .models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):
    """Создание сериализатора для преображения данных модели Category в байтовые объекты
    для последующего отображения их в json формате"""
    class Meta:
        model = Category
        fields = ["name", "img", "soft_delete", ]


class ProductSerializer(serializers.ModelSerializer):
    """Создание сериализатора для преображения данных модели Product в байтовые объекты
    для последующего отображения их в json формате"""
    class Meta:
        model = Product
        fields = ["category", "name", "image", "description", "discount", "price", "stock", "available", "sale_count",
                  "total_price", "soft_delete", ]


class ReviewSerializer(serializers.ModelSerializer):
    """Создание сериализатора для преображения данных модели Review в байтовые объекты
    для последующего отображения их в json формате"""
    class Meta:
        model = Review
        fields = ["review", "created_ad", "user", "products", "soft_delete"]




class ReviewPostSerializer(serializers.ModelSerializer):
    """Создание сериализатора для преображения данных модели Author в объекты python для отображения в json формате"""
    class Meta:
        model = Review
        fields = ["review", "products", ]
