from django.contrib import admin
from product.models import Product, subscription

# Register your models here.

admin.site.register(Product)
admin.site.register(subscription)