# Generated by Django 4.1.5 on 2023-03-09 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_remove_orderproduct_color_remove_orderproduct_size_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='variation',
            new_name='varation',
        ),
    ]
