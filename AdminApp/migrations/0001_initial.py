# Generated by Django 4.2.7 on 2023-11-29 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=50)),
                ('Category_description', models.CharField(max_length=100)),
                ('Category_Image', models.ImageField(default='null.jpg', upload_to='image')),
            ],
        ),
    ]
