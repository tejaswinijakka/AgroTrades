from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

#class User(auth.models.User, auth.models.PermissionsMixin):
    
#    def __str__(self):
#        return "@{}".format(self.name)

class Product(models.Model):
    name = models.CharField('Product Name',max_length = 100)
    product_id = models.AutoField(auto_created = True, primary_key=True)
    category = models.IntegerField(null = False)
    quantity = models.IntegerField(null = False)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

class WishList_Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    cart_wish = models.IntegerField(null = False)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    expiry_date = models.DateTimeField(null = False)

    def __str__(self):
        return self.name

class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    Comment_id = models.AutoField(auto_created = True, primary_key=True)
    Comment = models.TextField(blank = True)

    def __str__(self):
        return self.name

class Delivery(models.Model):
    delivery_id = models.AutoField(auto_created = True, primary_key=True)
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    Ratings = models.IntegerField(null = False)


    def __str__(self):
        return self.name



'''class Registration(models.Model):
    name = models.CharField(max_length=70, null = True)
    phno = PhoneNumberField(null=True, unique=False)
    password = models.CharField(max_length=50, null = True)
    location = models.CharField(max_length=50, null = True)
    usertype = models.IntegerField(null = True)'''
