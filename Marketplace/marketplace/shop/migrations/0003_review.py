# Generated by Django 4.1.7 on 2023-04-05 17:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_product_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, null=True, verbose_name='delivery_adress')),
                ('created_ad', models.DateTimeField(auto_now_add=True, verbose_name='created_ad')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='field-user_verbose')),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews',
            },
        ),
    ]
