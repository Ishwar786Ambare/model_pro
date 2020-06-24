from django.contrib import admin

from modelapp.models import Product, Vendor, Customer

admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(Customer)
