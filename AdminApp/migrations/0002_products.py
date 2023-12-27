# Generated by Django 4.2.7 on 2023-12-01 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=50)),
                ('Product_description', models.CharField(max_length=50)),
                ('Product_Image', models.ImageField(default='null.jpg', upload_to='image')),
            ],
        ),
    ]