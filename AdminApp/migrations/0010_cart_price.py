# Generated by Django 4.2.7 on 2023-12-11 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0009_alter_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]