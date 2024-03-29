# Generated by Django 4.2.7 on 2023-12-12 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0011_delete_cart'),
        ('Userapp', '0003_remove_cart_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=50)),
                ('Pincode', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.products')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.registration')),
            ],
        ),
    ]
