# Generated by Django 4.1.5 on 2023-02-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_variation_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('COLOR', 'color'), ('SIZE', 'size')], max_length=200),
        ),
    ]