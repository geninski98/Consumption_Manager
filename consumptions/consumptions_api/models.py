from django.db import models
from datetime import datetime
from django_unixdatetimefield import UnixDateTimeField

# Create your models here.
class ProductCategories(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=10, null=False)

    def __str__ (self):
        return self.code

class Products(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=25, null=False)
    category = models.ForeignKey(ProductCategories, to_field='code', on_delete=models.CASCADE)

    def __str__ (self):
        return self.code

class Consumptions(models.Model):
    timestamp = UnixDateTimeField(auto_now_add=True)
    product = models.ForeignKey(Products, to_field='code', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
