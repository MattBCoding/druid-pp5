# Generated by Django 3.2 on 2022-06-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220617_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this product should be treated as active. Unselect this instead of deleting products.', verbose_name='active'),
        ),
    ]