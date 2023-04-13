from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models import Product


class Order(models.Model):
    """Создаем модель Order"""
    class Meta:
        verbose_name_plural = _("orders")
        verbose_name = _("order")

    email = models.EmailField(max_length=30, verbose_name=_("email"))
    delivery_adress = models.TextField(null=True, blank=True, verbose_name=_("delivery_adress"))
    promocode = models.CharField(max_length=20, null=False, blank=True, verbose_name=_("promocode"))
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name=_("created_ad"))
    soft_delete = models.BooleanField(default=False, verbose_name=_("soft_delete"))

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """Создаем модель OrderItem для хранения информации о выполненных заказах"""
    order = models.ForeignKey(Order,on_delete=models.PROTECT, related_name='items')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_("field-user_verbose"))
    products = models.ForeignKey(Product,on_delete=models.PROTECT, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    soft_delete = models.BooleanField(default=False, verbose_name=_("soft_delete"))

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
