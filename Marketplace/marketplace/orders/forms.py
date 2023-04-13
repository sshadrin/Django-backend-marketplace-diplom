from django import forms

from .models import Order


class OrdersForm(forms.ModelForm):
    """Создаем форму с помощью модели формы для отрисовки шаблона по нашей модели"""
    class Meta:
        model = Order
        fields = ["email", "delivery_adress", "promocode",]