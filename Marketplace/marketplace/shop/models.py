from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def shop_img_directory_path(instance: "Shop", filename: str) -> str:
    """Создаем функцию для сохранения изображений категорий и продуктов"""
    return "shops/shop_{pk}/img/{filename}".format(pk=instance.pk, filename=filename)


class Category(models.Model):
    """Создаем модель Категория для работы с категориями"""
    name = models.CharField(max_length=200, db_index=True)
    img = models.ImageField(null=True, blank=True, upload_to=shop_img_directory_path)
    soft_delete = models.BooleanField(default=False, verbose_name=_("soft_delete"))

    class Meta:
        ordering = 'name',
        verbose_name = _('Category')
        verbose_name_plural = _('Categoryes')

    def __str__(self):
        return self.name


class Product(models.Model):
    """Создаем модель Продукты для работы с продуктами в категориях"""
    category = models.ForeignKey(Category, related_name=_('products'), on_delete=models.PROTECT,)
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    discount = models.SmallIntegerField(default=0, verbose_name=_("discount"))
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    sale_count = models.PositiveIntegerField(default=0, verbose_name="sale_count")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    soft_delete = models.BooleanField(default=False, verbose_name=_("soft_delete"))

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name

    def get_total_price(self):
        total = self.price * (100 - self.discount) / 100
        return total

    def save(self, *args, **kwargs):
        self.total_price = self.get_total_price()
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:products_details',
                       args=self.pk)


class Review(models.Model):
    """Создаем модель Отзывы для возможности добавления отзывов к продуктам"""
    class Meta:
        verbose_name_plural = _("reviews")
        verbose_name = _("review")

    review = models.TextField(null=True, blank=True, verbose_name=_("review"))
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name=_("created_ad"))
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_("field-user_verbose"))
    products = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name=_("products"))
    soft_delete = models.BooleanField(default=False, verbose_name=_("soft_delete"))