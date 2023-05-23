from django.db import models
import datetime
# from multiselectfield import MultiSelectField

class Category(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Products(models.Model):
    name = models.CharField(max_length=60)
    price= models.IntegerField(default=0)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image = models.ImageField(upload_to='product_images/')
    # image = MultiSelectField(choices=[('image1', 'Image 1'), ('image2', 'Image 2'), ('image3', 'Image 3')], blank=True)
    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)
    def __str__(self):
        return f"{self.product} - {self.customer}"




# using functions:
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Category, Customer, Products, Order
# from .serializers import CategorySerializer, CustomerSerializer, ProductSerializer, OrderSerializer

# # Category Views
# @api_view(['GET', 'POST'])
# def category_list(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def category_detail(request, pk):
#     try:
#         category = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         category.delete()
#         return Response(status=204)

# # Customer Views
# @api_view(['GET', 'POST'])
# def customer_list(request):
#     if request.method == 'GET':
#         customers = Customer.objects.all()
#         serializer = CustomerSerializer(customers, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def customer_detail(request, pk):
#     try:
#         customer = Customer.objects.get(pk=pk)
#     except Customer.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = CustomerSerializer(customer)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CustomerSerializer(customer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         customer.delete()
#         return Response(status=204)

# # Products Views
# @api_view(['GET', 'POST'])
# def products_list(request):
#     if request.method == 'GET':
#         products = Products.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def products_detail(request, pk):
#     try:
#         product = Products.objects.get(pk=pk)
#     except Products.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=204)

# # Order Views
# @api_view(['GET', 'POST'])
# def order_list(request):
#     if request.method == 'GET':
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def order_detail(request, pk):
#     try:
#         order = Order.objects.get(pk=pk)
#     except Order.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = OrderSerializer(order)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = OrderSerializer(order, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         order.delete()
#         return Response(status=204)

