# #using generics
# from rest_framework import generics
# from .models import Category, Customer, Products, Order
# from .serializers import CategorySerializer, CustomerSerializer, ProductSerializer, OrderSerializer

# class CategoryListCreateView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CustomerListCreateView(generics.ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

# class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

# class ProductListCreateView(generics.ListCreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer

# class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer

# class OrderListCreateView(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

# class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer



# # #class based:
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Category, Customer, Products, Order
# from .serializers import CategorySerializer, CustomerSerializer, ProductSerializer, OrderSerializer

# class CategoryListCreateView(APIView):
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CategoryRetrieveUpdateDestroyView(APIView):
#     def get_object(self, pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         category = self.get_object(pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         category = self.get_object(pk)
#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         category = self.get_object(pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class CustomerListCreateView(APIView):
#     def get(self, request):
#         customers = Customer.objects.all()
#         serializer = CustomerSerializer(customers, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CustomerRetrieveUpdateDestroyView(APIView):
#     def get_object(self, pk):
#         try:
#             return Customer.objects.get(pk=pk)
#         except Customer.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         customer = self.get_object(pk)
#         serializer = CustomerSerializer(customer)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         customer = self.get_object(pk)
#         serializer = CustomerSerializer(customer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         customer = self.get_object(pk)
#         customer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ProductListCreateView(APIView):
#     def get(self, request):
#         products = Products.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProductRetrieveUpdateDestroyView(APIView):
#     def get_object(self, pk):
#         try:
#             return Products.objects.get(pk=pk)
#         except Products.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         product = self.get_object(pk)
#         # serializer = ProductSerializer(product,data=request.DATA, files=request.FILES)
#         serializer = ProductSerializer(product,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         product = self.get_object(pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class OrderListCreateView(APIView):
#     def get(self, request):
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class OrderRetrieveUpdateDestroyView(APIView):
#     def get_object(self, pk):
#         try:
#             return Order.objects.get(pk=pk)
#         except Order.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         order = self.get_object(pk)
#         serializer = OrderSerializer(order)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         order = self.get_object(pk)
#         serializer = OrderSerializer(order, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         order = self.get_object(pk)
#         order.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)







# ## function based:
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Category, Customer, Products, Order
# from .serializers import CategorySerializer, CustomerSerializer, ProductSerializer, OrderSerializer

# # Category Views
# @api_view(['GET', 'POST'])
# def category_list(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True, context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data,context={'request': request})
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
#         serializer = CategorySerializer(category, context={'request': request})
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
#         serializer = CustomerSerializer(customers, many=True, context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CustomerSerializer(data=request.data,context={'request': request})
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
#         serializer = CustomerSerializer(customer, context={'request': request})
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
#         serializer = ProductSerializer(products, many=True, context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data,context={'request': request})
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
#         serializer = ProductSerializer(product,context={'request': request})
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
#         serializer = OrderSerializer(orders, many=True, context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = OrderSerializer(data=request.data,context={'request': request})
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
#         serializer = OrderSerializer(order,context={'request': request})
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
    


# # friday task:
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Cart, CartItem
# from .serializers import CartSerializer, CartItemSerializer

# # Cart Views
# @api_view(['GET', 'POST'])
# def cart_list(request):
#     if request.method == 'GET':
#         carts = Cart.objects.all()
#         serializer = CartSerializer(carts, many=True, context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CartSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def cart_detail(request, pk):
#     try:
#         cart = Cart.objects.get(pk=pk)
#     except Cart.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = CartSerializer(cart, context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CartSerializer(cart, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         cart.delete()
#         return Response(status=204)

# # CartItem Views
# @api_view(['GET', 'POST'])
# def cartitem_list(request):
#     if request.method == 'GET':
#         cart_items = CartItem.objects.all()
#         serializer = CartItemSerializer(cart_items, many=True, context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CartItemSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def cartitem_detail(request, pk):
#     try:
#         cart_item = CartItem.objects.get(pk=pk)
#     except CartItem.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = CartItemSerializer(cart_item, context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CartItemSerializer(cart_item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         cart_item.delete()
#         return Response(status=204)




# used Authentication on e-commerce api:

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 
from django.contrib.auth import authenticate, login, logout
from .models import Category,Products, Order, Cart, CartItem, CustomerProfile
from .serializers import CustomerProfileSerializer,CategorySerializer, CustomerSerializer, ProductSerializer, OrderSerializer, CartSerializer, CartItemSerializer
from rest_framework.permissions import IsAuthenticated  

@api_view(['POST'])
def customer_register(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        
        return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=400)



@api_view(['POST'])
def customer_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'})
    else:
        return Response({'message': 'Invalid credentials'}, status=401)
    

@api_view(['POST'])
def customer_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return Response({'message': 'Logout successful'})
    else:
        return Response({'error': 'User is not authenticated'}, status=401)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def customer_profile_view(request):
    if request.method == 'GET':
        profiles = CustomerProfile.objects.filter(customer=request.user)  # Filter profiles by the authenticated customer
        serializer = CustomerProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(customer=request.user)  # Set the customer field to the authenticated user
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def customer_profile_detail_view(request, pk):
    try:
        profile = CustomerProfile.objects.get(pk=pk)
    except CustomerProfile.DoesNotExist:
        return Response(status=404)

    # Check if the authenticated customer is the owner of the profile
    if profile.customer != request.user:
        return Response({'message': 'You are not authorized to access this profile.'}, status=403)

    if request.method == 'GET':
        serializer = CustomerProfileSerializer(profile)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = CustomerProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def products_list(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def products_detail(request, pk):
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def cart_list(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def cart_detail(request, pk):
    try:
        cart = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CartSerializer(cart)

        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        cart.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def cart_item_list(request):
    if request.method == 'GET':
        cart_items = CartItem.objects.all()
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def cart_item_detail(request, pk):
    try:
        cart_item = CartItem.objects.get(pk=pk)
    except CartItem.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = CartItemSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        cart_item.delete()
        return Response(status=204)
    




# @api_view(['POST'])
# def customer_register(request):
#     serializer = CustomerSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         user.set_password(request.data.get('password'))
#         user.save()
        
#         # Create a profile for the registered customer
#         profile_data = {
#             'customer': user,
#             'fullname': user.fullname,
#             'phone': user.phone,
#             'email': user.email,
#             'password': user.password
#         }
#         profile_serializer = CustomerProfileSerializer(data=profile_data)
#         if profile_serializer.is_valid():
#             profile_serializer.save()
        
#         # Log in the registered customer
#         login(request, user)
        
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)


# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def customer_profile_view(request):
#     if request.method == 'GET':
#         profiles = CustomerProfile.objects.all()
#         serializer = CustomerProfileSerializer(profiles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CustomerProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def customer_profile_detail_view(request, pk):
#     try:
#         profile = CustomerProfile.objects.get(pk=pk)
#     except CustomerProfile.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = CustomerProfileSerializer(profile)
#         return Response(serializer.data)
#     elif request.method == 'PUT' or request.method == 'PATCH':
#         serializer = CustomerProfileSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         profile.delete()
#         return Response(status=204)