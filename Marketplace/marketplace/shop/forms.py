from django import forms

from .models import Category, Product, Review


class CategoryForm(forms.ModelForm):
    """Создаем форму для отрисовки шаблона по нашей модели"""
    class Meta:
        model = Category
        fields = "name",


class ProductForm(forms.ModelForm):
    """Создаем форму для отрисовки шаблона по нашей модели"""
    class Meta:
        model = Product
        fields = ["name", "description", "discount", "price", "stock", "sale_count"]


class ReviewForm(forms.ModelForm):
    """Создаем форму для отрисовки шаблона по нашей модели"""
    class Meta:
        model = Review
        fields = ["review", ]