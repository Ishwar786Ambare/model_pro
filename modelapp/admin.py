from django.contrib import admin
from modelapp.models import Customer, Products, Vendor


class CustomerAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(Products)

# , Vendor, Customer

# admin.site.register(Product)
# admin.site.register(Vendor)
