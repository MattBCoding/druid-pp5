# Generated by Django 3.2 on 2022-06-17 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_has_colours'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='highlights',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='technical_details',
            field=models.TextField(blank=True),
        ),
    ]
