# Generated by Django 5.0.6 on 2024-06-13 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_total_cart_grandtotal_remove_cartitem_cart_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='optionlist',
            old_name='Options',
            new_name='options',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='OptionsLists',
            new_name='optionsLists',
        ),
    ]