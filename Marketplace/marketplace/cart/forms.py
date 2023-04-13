from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 6)]


class CartAddProductForm(forms.Form):
    """Форма для отображения количества товара в шаблоне, с возможным его добавлением"""
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)