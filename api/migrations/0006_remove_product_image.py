# Generated by Django 5.0.6 on 2024-06-15 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]