# Generated by Django 4.1.5 on 2023-03-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_rename_variation_orderproduct_varation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_oredered',
            field=models.BooleanField(default=True),
        ),
    ]