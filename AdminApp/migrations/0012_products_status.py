# Generated by Django 4.2.7 on 2023-12-15 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0011_delete_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
