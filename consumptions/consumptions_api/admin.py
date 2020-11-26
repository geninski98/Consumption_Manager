from django.contrib import admin
from .models import ProductCategories, Products, Consumptions

# Register your models here.
admin.site.register(ProductCategories)
admin.site.register(Products)
admin.site.register(Consumptions)