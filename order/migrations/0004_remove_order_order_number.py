# Generated by Django 4.1.5 on 2023-03-07 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_number',
        ),
    ]
