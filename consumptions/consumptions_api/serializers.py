from rest_framework import serializers
from .models import ProductCategories, Products, Consumptions

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategories
        fields = ['id','code','name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id','code','name','category']

class ConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumptions
        fields = ['id','timestamp','product','quantity']