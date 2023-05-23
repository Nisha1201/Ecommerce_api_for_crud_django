from rest_framework import serializers
from .models import Category, Customer, Products, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = Products
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


        
