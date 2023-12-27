from django.db import models
from AdminApp.models import*

# Create your models here.
class Cart(models.Model):
     user_id = models.ForeignKey(Registration, on_delete=models.CASCADE)
     product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
     total_amt = models.FloatField()
     quantity = models.IntegerField(null=True)
     status=models.IntegerField(default=0)
class Order(models.Model):
     Address = models.CharField(max_length=100)
     town = models.CharField(max_length=50)
     Pincode=models.CharField(max_length=9)
     user_id = models.ForeignKey(Registration, on_delete=models.CASCADE)
     cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True)
     status=models.IntegerField(default=0)
    


     