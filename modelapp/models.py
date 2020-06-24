from django.db import models
from datetime import datetime as dt


class Common(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        # model = Common
        abstract = True


class Executive(models.Model):
    pass


class Service_Uplode(models.Model):
    pass


class Service_Assign(models.Model):
    pass


class Employee(models.Model):
    pass


class Vendor(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    v_p = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    discription = models.TextField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True, max_length=100)
    # date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=100)
