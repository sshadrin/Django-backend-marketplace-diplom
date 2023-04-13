from rest_framework import viewsets
from .models import Category, Product, Review


class CategoryViewSet(viewsets.ModelViewSet):
    """Создание API представлений модели Category в django rest framework"""
    queryset = Category.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    """Создание API представлений модели Product в django rest framework"""
    queryset = Product.objects.all()


class ReviewViewSet(viewsets.ModelViewSet):
    """Создание API представлений модели Review в django rest framework"""
    queryset = Review.objects.all()