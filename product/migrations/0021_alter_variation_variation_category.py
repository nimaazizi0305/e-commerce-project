# Generated by Django 4.1.5 on 2023-03-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_alter_variation_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('COLOR', 'color'), ('SIZE', 'size')], max_length=200),
        ),
    ]
