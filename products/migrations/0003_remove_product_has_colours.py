# Generated by Django 3.2 on 2022-06-17 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220617_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_colours',
        ),
    ]
