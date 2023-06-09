# Generated by Django 4.1.7 on 2023-04-05 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_products_remove_order_user_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='soft_delete',
            field=models.BooleanField(default=False, verbose_name='soft_delete'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='soft_delete',
            field=models.BooleanField(default=False, verbose_name='soft_delete'),
        ),
    ]
