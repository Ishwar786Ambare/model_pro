from django.db import models


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
    pass


class Product(models.Model):
    v_p = models.ForeignKey(Vendor, on_delete=models.CASCADE)


class Customer(models.Model):
    pass
