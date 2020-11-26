from django.db import models

# Create your models here.
class ProductCategories(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=10, null=False)

class Products(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=25, null=False)
    category = models.ForeignKey(ProductCategories, to_field='code', on_delete=models.CASCADE)

class Consumptions(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Products, to_field='code', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

