# Generated by Django 4.1.5 on 2023-03-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_alter_variation_variation_category'),
        ('order', '0011_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='product.product'),
        ),
    ]
