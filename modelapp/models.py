from django.db import models
from datetime import datetime as dt



class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    # password = models.PasswordField(max_length=100)
    address = models.CharField(max_length=100)


class Vendor(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default='vendor')
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    weight = models.DecimalField(max_digits=100, decimal_places=3, default=0, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stock = models.BigIntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="media/")

    def __str__(self):
        return self.name
