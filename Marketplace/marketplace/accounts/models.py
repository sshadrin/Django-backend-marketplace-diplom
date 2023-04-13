from django.contrib.auth.models import User
from django.db import models


def profile_avatar_directory_path(instance: "Profile", filename: str) -> str:
    return "profiles/profile_{pk}/avatar/{filename}".format(pk=instance.pk, filename=filename)


class Profile(models.Model):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    balance = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name=("balance"))
    agreement_accepted = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True, upload_to=profile_avatar_directory_path)
