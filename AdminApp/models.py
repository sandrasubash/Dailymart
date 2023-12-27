from django.db import models

# Create your models here.
class Category(models.Model):
    Category_name=models.CharField(max_length=50)
    Category_description=models.CharField(max_length=100)
    Category_Image=models.ImageField(upload_to='image',default='null.jpg')
class Products(models.Model):
    Product_name=models.CharField(max_length=50)
    Product_category=models.CharField(max_length=50, default='null')
    Product_description=models.CharField(max_length=50)
    Product_price=models.IntegerField(null=True,blank=True)
    Image=models.ImageField(upload_to='image',default='null.jpg')
    status=models.IntegerField(default=0)

class Contact(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Message=models.CharField(max_length=100)


class Registration(models.Model):
      Name=models.CharField(max_length=50)
      Email=models.EmailField(max_length=50)
      Phone=models.CharField(max_length=10)
      Password=models.CharField(max_length=100)



