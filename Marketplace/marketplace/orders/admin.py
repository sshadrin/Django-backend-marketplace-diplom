from django.contrib import admin
from django.db.models import QuerySet

from .models import Order


@admin.action(description="Soft delete object")
def soft_delete(queryset: QuerySet):
    """Добавляем функцию возможности мягкого удаления заказа в админку"""
    queryset.update(soft_delete=True)


@admin.action(description="Restore object")
def restore(queryset: QuerySet):
    """Добавляем функцию возможности восстановления удаленого заказа в админке"""
    queryset.update(soft_delete=False)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Добавляем функцию для работы с моделью Order в админке"""
    actions = [
        soft_delete,
        restore,
    ]
    list_display = ["email", "delivery_adress", "promocode", "created_ad", "soft_delete",]
