# Generated by Django 4.1.5 on 2023-02-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_rename_price_cartitems_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]