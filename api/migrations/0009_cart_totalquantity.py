# Generated by Django 5.0.6 on 2024-06-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_cart_cartitems_alter_cart_grandtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='totalQuantity',
            field=models.IntegerField(default=0),
        ),
    ]
