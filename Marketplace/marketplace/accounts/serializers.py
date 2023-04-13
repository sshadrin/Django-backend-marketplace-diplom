from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Создание сериализатора для преображения данных модели Profile в байтовые объекты
    для последующего отображения их в json формате"""
    class Meta:
        model = Profile
        fields = ["user", "bio", "balance", "agreement_accepted", "avatar", ]
