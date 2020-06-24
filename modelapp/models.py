from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default='vendor')
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=True, null=True, default=9066371333)
    address = models.CharField(max_length=100, blank=True, null=True, default="hyd")

    def __str__(self):
        return self.name


class Products(models.Model):
    PtoV = models.ForeignKey(Vendor, on_delete=models.CASCADE, )
    name_of_product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    weight = models.DecimalField(max_digits=100, decimal_places=3, default=0, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stock = models.BigIntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="media/")

    def __str__(self):
        return self.name_of_product


class Customer(models.Model):
    order = models.ManyToManyField(Products, blank=True, )
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default="customer@gmail.com")
    mobile = models.BigIntegerField(default=9066371333)
    # password = models.PasswordField(max_length=100)
    address = models.CharField(max_length=100)


class ServiceUplode(models.Model):
    pass


class ServiceAssign(models.Model):
    pass
