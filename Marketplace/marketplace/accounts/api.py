from rest_framework import viewsets
from .models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    """Создание API представлений модели Profile в django rest framework"""
    queryset = Profile.objects.all()

