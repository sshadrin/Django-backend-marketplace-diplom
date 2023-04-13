from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    verbose_name = gettext_lazy("orders")
