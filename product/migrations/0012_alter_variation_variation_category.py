# Generated by Django 4.1.5 on 2023-03-07 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_variation_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('SIZE', 'size'), ('COLOR', 'color')], max_length=200),
        ),
    ]
