# Generated by Django 4.2.7 on 2023-12-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0005_rename_product_image_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Product_price',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
