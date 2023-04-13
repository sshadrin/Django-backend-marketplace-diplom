from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    """Создаем форму для отрисовки шаблона по нашей модели Profile"""
    class Meta:
        model = Profile
        fields = ["bio", "avatar", ]