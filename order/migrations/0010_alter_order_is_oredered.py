# Generated by Django 4.1.5 on 2023-03-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_order_is_oredered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_oredered',
            field=models.BooleanField(default=False),
        ),
    ]
