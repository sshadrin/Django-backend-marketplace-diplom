from django.contrib import admin
from django.db.models import QuerySet

from .models import Category, Product, Review


@admin.action(description="Soft delete object")
def soft_delete(queryset: QuerySet):
    """Добавляем функцию возможности мягкого удаления продукта и категории в админку"""
    queryset.update(soft_delete=True)


@admin.action(description="Restore object")
def restore(queryset: QuerySet):
    """Добавляем функцию возможности восстановления удаленого продукта или категории в админке"""
    queryset.update(soft_delete=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Добавляем функцию для работы с моделью категории в админке"""
    actions = [
        soft_delete,
        restore,
    ]
    list_display = ['name', 'img', 'soft_delete', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Добавляем функцию для работы с моделью продукты в админке"""
    actions = [
        soft_delete,
        restore,
    ]
    readonly_fields = ('total_price',)
    list_display = ['name', 'price', 'stock', 'available', 'discount', "total_price", 'soft_delete', ]
    list_filter = ['available', ]
    list_editable = ['price', 'stock', 'available', 'discount', ]


@admin.register(Review)
class ProductAdmin(admin.ModelAdmin):
    """Добавляем функцию для работы с моделью отзывыr в админке"""
    actions = [
        soft_delete,
        restore,
    ]
    list_display = ['review', 'soft_delete', ]