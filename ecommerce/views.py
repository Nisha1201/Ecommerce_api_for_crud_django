# # #using generics
# # from rest_framework import generics
# # from .models import Category, Customer, Products, Order
# # from .serializers import CategorySerializer, CustomerSerializer, ProductSerializer, OrderSerializer

# # class CategoryListCreateView(generics.ListCreateAPIView):
# #     queryset = Category.objects.all()
# #     serializer_class = CategorySerializer

# # class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Category.objects.all()
# #     serializer_class = CategorySerializer

# # class CustomerListCreateView(generics.ListCreateAPIView):
# #     queryset = Customer.objects.all()
# #     serializer_class = CustomerSerializer

# # class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Customer.objects.all()
# #     serializer_class = CustomerSerializer

# # class ProductListCreateView(generics.ListCreateAPIView):
# #     queryset = Products.objects.all()
# #     serializer_class = ProductSerializer

# # class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Products.objects.all()
# #     serializer_class = ProductSerializer

# # class OrderListCreateView(generics.ListCreateAPIView):
# #     queryset = Order.objects.all()
# #     serializer_class = OrderSerializer

# # class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Order.objects.all()
# #     serializer_class = OrderSerializer



# # # #class based:
# # from django.http import Http404
# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status
# # from .models import Category, Customer, Products, Order
# # from .serializers import CategorySerializer, CustomerSerializer, ProductSerializer, OrderSerializer

# # class CategoryListCreateView(APIView):
# #     def get(self, request):
# #         categories = Category.objects.all()
# #         serializer = CategorySerializer(categories, many=True)
# #         return Response(serializer.data)

# #     def post(self, request):
# #         serializer = CategorySerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # class CategoryRetrieveUpdateDestroyView(APIView):
# #     def get_object(self, pk):
# #         try:
# #             return Category.objects.get(pk=pk)
# #         except Category.DoesNotExist:
# #             raise Http404

# #     def get(self, request, pk):
# #         category = self.get_object(pk)
# #         serializer = CategorySerializer(category)
# #         return Response(serializer.data)

# #     def put(self, request, pk):
# #         category = self.get_object(pk)
# #         serializer = CategorySerializer(category, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def delete(self, request, pk):
# #         category = self.get_object(pk)
# #         category.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)


# # class CustomerListCreateView(APIView):
# #     def get(self, request):
# #         customers = Customer.objects.all()
# #         serializer = CustomerSerializer(customers, many=True)
# #         return Response(serializer.data)

# #     def post(self, request):
# #         serializer = CustomerSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # class CustomerRetrieveUpdateDestroyView(APIView):
# #     def get_object(self, pk):
# #         try:
# #             return Customer.objects.get(pk=pk)
# #         except Customer.DoesNotExist:
# #             raise Http404

# #     def get(self, request, pk):
# #         customer = self.get_object(pk)
# #         serializer = CustomerSerializer(customer)
# #         return Response(serializer.data)

# #     def put(self, request, pk):
# #         customer = self.get_object(pk)
# #         serializer = CustomerSerializer(customer, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def delete(self, request, pk):
# #         customer = self.get_object(pk)
# #         customer.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)


# # class ProductListCreateView(APIView):
# #     def get(self, request):
# #         products = Products.objects.all()
# #         serializer = ProductSerializer(products, many=True)
# #         return Response(serializer.data)

# #     def post(self, request):
# #         serializer = ProductSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # class ProductRetrieveUpdateDestroyView(APIView):
# #     def get_object(self, pk):
# #         try:
# #             return Products.objects.get(pk=pk)
# #         except Products.DoesNotExist:
# #             raise Http404

# #     def get(self, request, pk):
# #         product = self.get_object(pk)
# #         serializer = ProductSerializer(product)
# #         return Response(serializer.data)

# #     def put(self, request, pk):
# #         product = self.get_object(pk)
# #         # serializer = ProductSerializer(product,data=request.DATA, files=request.FILES)
# #         serializer = ProductSerializer(product,data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def delete(self, request, pk):
# #         product = self.get_object(pk)
# #         product.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)


# # class OrderListCreateView(APIView):
# #     def get(self, request):
# #         orders = Order.objects.all()
# #         serializer = OrderSerializer(orders, many=True)
# #         return Response(serializer.data)

# #     def post(self, request):
# #         serializer = OrderSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # class OrderRetrieveUpdateDestroyView(APIView):
# #     def get_object(self, pk):
# #         try:
# #             return Order.objects.get(pk=pk)
# #         except Order.DoesNotExist:
# #             raise Http404

# #     def get(self, request, pk):
# #         order = self.get_object(pk)
# #         serializer = OrderSerializer(order)
# #         return Response(serializer.data)

# #     def put(self, request, pk):
# #         order = self.get_object(pk)
# #         serializer = OrderSerializer(order, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def delete(self, request, pk):
# #         order = self.get_object(pk)
# #         order.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)







# # ## function based:
# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response
# # from .models import Category, Customer, Products, Order
# # from .serializers import CategorySerializer, CustomerSerializer, ProductSerializer, OrderSerializer

# # # Category Views
# # @api_view(['GET', 'POST'])
# # def category_list(request):
# #     if request.method == 'GET':
# #         categories = Category.objects.all()
# #         serializer = CategorySerializer(categories, many=True, context={'request': request})
# #         return Response(serializer.data)

# #     elif request.method == 'POST':
# #         serializer = CategorySerializer(data=request.data,context={'request': request})
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=201)
# #         return Response(serializer.errors, status=400)

# # @api_view(['GET', 'PUT', 'DELETE'])
# # def category_detail(request, pk):
# #     try:
# #         category = Category.objects.get(pk=pk)
# #     except Category.DoesNotExist:
# #         return Response(status=404)

# #     if request.method == 'GET':
# #         serializer = CategorySerializer(category, context={'request': request})
# #         return Response(serializer.data)

# #     elif request.method == 'PUT':
# #         serializer = CategorySerializer(category, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=400)

# #     elif request.method == 'DELETE':
# #         category.delete()
# #         return Response(status=204)

# # # Customer Views
# # @api_view(['GET', 'POST'])
# # def customer_list(request):
# #     if request.method == 'GET':
# #         customers = Customer.objects.all()
# #         serializer = CustomerSerializer(customers, many=True, context={'request': request})
# #         return Response(serializer.data)

# #     elif request.method == 'POST':
# #         serializer = CustomerSerializer(data=request.data,context={'request': request})
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=201)
# #         return Response(serializer.errors, status=400)

# # @api_view(['GET', 'PUT', 'DELETE'])
# # def customer_detail(request, pk):
# #     try:
# #         customer = Customer.objects.get(pk=pk)
# #     except Customer.DoesNotExist:
# #         return Response(status=404)

# #     if request.method == 'GET':
# #         serializer = CustomerSerializer(customer, context={'request': request})
# #         return Response(serializer.data)

# #     elif request.method == 'PUT':
# #         serializer = CustomerSerializer(customer, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=400)

# #     elif request.method == 'DELETE':
# #         customer.delete()
# #         return Response(status=204)

# # # Products Views
# # @api_view(['GET', 'POST'])
# # def products_list(request):
# #     if request.method == 'GET':
# #         products = Products.objects.all()
# #         serializer = ProductSerializer(products, many=True, context={'request': request})
# #         return Response(serializer.data)

# #     elif request.method == 'POST':
# #         serializer = ProductSerializer(data=request.data,context={'request': request})
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=201)
# #         return Response(serializer.errors, status=400)

# # @api_view(['GET', 'PUT', 'DELETE'])
# # def products_detail(request, pk):
# #     try:
# #         product = Products.objects.get(pk=pk)
# #     except Products.DoesNotExist:
# #         return Response(status=404)

# #     if request.method == 'GET':
# #         serializer = ProductSerializer(product,context={'request': request})
# #         return Response(serializer.data)

# #     elif request.method == 'PUT':
# #         serializer = ProductSerializer(product, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=400)

# #     elif request.method == 'DELETE':
# #         product.delete()
# #         return Response(status=204)

# # # Order Views
# # @api_view(['GET', 'POST'])
# # def order_list(request):
# #     if request.method == 'GET':
# #         orders = Order.objects.all()
# #         serializer = OrderSerializer(orders, many=True, context={'request': request})
# #         return Response(serializer.data)

# #     elif request.method == 'POST':
# #         serializer = OrderSerializer(data=request.data,context={'request': request})
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=201)
# #         return Response(serializer.errors, status=400)

# # @api_view(['GET', 'PUT', 'DELETE'])
# # def order_detail(request, pk):
# #     try:
# #         order = Order.objects.get(pk=pk)
# #     except Order.DoesNotExist:
# #         return Response(status=404)

# #     if request.method == 'GET':
# #         serializer = OrderSerializer(order,context={'request': request})
# #         return Response(serializer.data)

# #     elif request.method == 'PUT':
# #         serializer = OrderSerializer(order, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=400)

# #     elif request.method == 'DELETE':
# #         order.delete()
# #         return Response(status=204)
    


# # # friday task:
# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response
# # from .models import Cart, CartItem
# # from .serializers import CartSerializer, CartItemSerializer

# # # Cart Views
# # @api_view(['GET', 'POST'])
# # def cart_list(request):
# #     if request.method == 'GET':
# #         carts = Cart.objects.all()
# #         serializer = CartSerializer(carts, many=True, context={'request': request})
# #         return Response(serializer.data)

# #     elif request.method == 'POST':
# #         serializer = CartSerializer(data=request.data, context={'request': request})
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=201)
# #         return Response(serializer.errors, status=400)

# # @api_view(['GET', 'PUT', 'DELETE'])
# # def cart_detail(request, pk):
# #     try:
# #         cart = Cart.objects.get(pk=pk)
# #     except Cart.DoesNotExist:
# #         return Response(status=404)

# #     if request.method == 'GET':
# #         serializer = CartSerializer(cart, context={'request': request})
# #         return Response(serializer.data)

# #     elif request.method == 'PUT':
# #         serializer = CartSerializer(cart, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=400)

# #     elif request.method == 'DELETE':
# #         cart.delete()
# #         return Response(status=204)

# # # CartItem Views
# # @api_view(['GET', 'POST'])
# # def cartitem_list(request):
# #     if request.method == 'GET':
# #         cart_items = CartItem.objects.all()
# #         serializer = CartItemSerializer(cart_items, many=True, context={'request': request})
# #         return Response(serializer.data)

# #     elif request.method == 'POST':
# #         serializer = CartItemSerializer(data=request.data, context={'request': request})
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=201)
# #         return Response(serializer.errors, status=400)

# # @api_view(['GET', 'PUT', 'DELETE'])
# # def cartitem_detail(request, pk):
# #     try:
# #         cart_item = CartItem.objects.get(pk=pk)
# #     except CartItem.DoesNotExist:
# #         return Response(status=404)

# #     if request.method == 'GET':
# #         serializer = CartItemSerializer(cart_item, context={'request': request})
# #         return Response(serializer.data)

# #     elif request.method == 'PUT':
# #         serializer = CartItemSerializer(cart_item, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=400)

# #     elif request.method == 'DELETE':
# #         cart_item.delete()
# #         return Response(status=204)




# # used Authentication on e-commerce api:

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response 
# from django.contrib.auth import authenticate, login, logout
# from .models import Category,Products, Order, Cart, CartItem, CustomerProfile
# from .serializers import CustomerProfileSerializer,CategorySerializer, CustomerSerializer, ProductSerializer, OrderSerializer, CartSerializer, CartItemSerializer
# from rest_framework.permissions import IsAuthenticated 
# from rest_framework_simplejwt.tokens import RefreshToken 

# @api_view(['POST'])
# def customer_register(request):
#     serializer = CustomerSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         user.set_password(request.data.get('password'))
#         user.save()
        
#         return Response(serializer.data, status=201)
    
#     return Response(serializer.errors, status=400)



# # @api_view(['POST'])
# # def customer_login(request):
# #     email = request.data.get('email')
# #     password = request.data.get('password')

# #     user = authenticate(request, email=email, password=password)

# #     if user is not None:
# #         login(request, user)
# #         return Response({'message': 'Login successful'})
# #     else:
# #         return Response({'message': 'Invalid credentials'}, status=401)
    
# @api_view(['POST'])
# def customer_login(request):
#     email = request.data.get('email')
#     password = request.data.get('password')

#     user = authenticate(request, email=email, password=password)

#     if user is not None:
#         login(request, user)

#         # Generate JWT access and refresh tokens
#         refresh = RefreshToken.for_user(user)
#         access_token = str(refresh.access_token)

#         return Response({'access_token': access_token,'refresh_token':str(refresh)})
#     else:
#         return Response({'message': 'Invalid credentials'}, status=401)


# @api_view(['POST'])
# def customer_logout(request):
#     if request.user.is_authenticated:
#         logout(request)
#         return Response({'message': 'Logout successful'})
#     else:
#         return Response({'error': 'User is not authenticated'}, status=401)


# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def customer_profile_view(request):
#     if request.method == 'GET':
#         profiles = CustomerProfile.objects.filter(customer=request.user)  # Filter profiles by the authenticated customer
#         serializer = CustomerProfileSerializer(profiles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CustomerProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(customer=request.user)  # Set the customer field to the authenticated user
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def customer_profile_detail_view(request, pk):
#     try:
#         profile = CustomerProfile.objects.get(pk=pk)
#     except CustomerProfile.DoesNotExist:
#         return Response(status=404)

#     # Check if the authenticated customer is the owner of the profile
#     if profile.customer != request.user:
#         return Response({'message': 'You are not authorized to access this profile.'}, status=403)

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

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
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

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def category_detail(request, pk):
#     try:
#         category = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     elif request.method == 'PUT' or request.method == 'PATCH':
#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         category.delete()
#         return Response(status=204)

# @api_view(['GET', 'POST'])
# # @permission_classes([IsAuthenticated])
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

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def products_detail(request, pk):
#     try:
#         product = Products.objects.get(pk=pk)
#     except Products.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     elif request.method == 'PUT' or request.method == 'PATCH':
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=204)

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
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

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def order_detail(request, pk):
#     try:
#         order = Order.objects.get(pk=pk)
#     except Order.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = OrderSerializer(order)
#         return Response(serializer.data)
#     elif request.method == 'PUT' or request.method == 'PATCH':
#         serializer = OrderSerializer(order, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         order.delete()
#         return Response(status=204)

# @api_view(['GET', 'POST'])
# # @permission_classes([IsAuthenticated])
# def cart_list(request):
#     if request.method == 'GET':
#         carts = Cart.objects.all()
#         serializer = CartSerializer(carts, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CartSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# # @permission_classes([IsAuthenticated])
# def cart_detail(request, pk):
#     try:
#         cart = Cart.objects.get(pk=pk)
#     except Cart.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = CartSerializer(cart)

#         return Response(serializer.data)
#     elif request.method == 'PUT' or request.method == 'PATCH':
#         serializer = CartSerializer(cart, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         cart.delete()
#         return Response(status=204)

# @api_view(['GET', 'POST'])
# # @permission_classes([IsAuthenticated])
# def cart_item_list(request):
#     if request.method == 'GET':
#         cart_items = CartItem.objects.all()
#         serializer = CartItemSerializer(cart_items, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CartItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# # @permission_classes([IsAuthenticated])
# def cart_item_detail(request, pk):
#     try:
#         cart_item = CartItem.objects.get(pk=pk)
#     except CartItem.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = CartItemSerializer(cart_item)
#         return Response(serializer.data)
#     elif request.method == 'PUT' or request.method == 'PATCH':
#         serializer = CartItemSerializer(cart_item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         cart_item.delete()
#         return Response(status=204)
    

# # wishlist________________________
# from .models import Wishlist
# from .serializers import WishlistSerializer

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def wishlist_list(request):
#     if request.method == 'GET':
#         wishlists = Wishlist.objects.all()
#         serializer = WishlistSerializer(wishlists, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = WishlistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def wishlist_detail(request, pk):
#     try:
#         wishlist = Wishlist.objects.get(pk=pk)
#     except Wishlist.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = WishlistSerializer(wishlist)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = WishlistSerializer(wishlist, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         wishlist.delete()
#         return Response(status=204)
    




# # @api_view(['POST'])
# # def customer_register(request):
# #     serializer = CustomerSerializer(data=request.data)
# #     if serializer.is_valid():
# #         user = serializer.save()
# #         user.set_password(request.data.get('password'))
# #         user.save()
        
# #         # Create a profile for the registered customer
# #         profile_data = {
# #             'customer': user,
# #             'fullname': user.fullname,
# #             'phone': user.phone,
# #             'email': user.email,
# #             'password': user.password
# #         }
# #         profile_serializer = CustomerProfileSerializer(data=profile_data)
# #         if profile_serializer.is_valid():
# #             profile_serializer.save()
        
# #         # Log in the registered customer
# #         login(request, user)
        
# #         return Response(serializer.data, status=201)
# #     return Response(serializer.errors, status=400)


# # @api_view(['GET', 'POST'])
# # @permission_classes([IsAuthenticated])
# # def customer_profile_view(request):
# #     if request.method == 'GET':
# #         profiles = CustomerProfile.objects.all()
# #         serializer = CustomerProfileSerializer(profiles, many=True)
# #         return Response(serializer.data)
# #     elif request.method == 'POST':
# #         serializer = CustomerProfileSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=201)
# #         return Response(serializer.errors, status=400)

# # @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# # @permission_classes([IsAuthenticated])
# # def customer_profile_detail_view(request, pk):
# #     try:
# #         profile = CustomerProfile.objects.get(pk=pk)
# #     except CustomerProfile.DoesNotExist:
# #         return Response(status=404)

# #     if request.method == 'GET':
# #         serializer = CustomerProfileSerializer(profile)
# #         return Response(serializer.data)
# #     elif request.method == 'PUT' or request.method == 'PATCH':
# #         serializer = CustomerProfileSerializer(profile, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=400)
# #     elif request.method == 'DELETE':
# #         profile.delete()
# #         return Response(status=204)




from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# @api_view(['POST'])
# def customer_registration_view(request):
#     if request.method == 'POST':
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             user = User.objects.create_user(
#                 username=serializer.validated_data['email'],
#                 email=serializer.validated_data['email'],
#                 password=request.data['password']
#             )
#             customer = Customer.objects.create(
#                 user=user,
#                 name=serializer.validated_data['name'],
#                 email=serializer.validated_data['email'],
#                 phone_number=serializer.validated_data['phone_number']
#             )
            

#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import Http404

from .models import Customer, Product, Order, OrderItem
from .serializers import (
    CustomerRegistrationSerializer,
    CustomerLoginSerializer,
    CustomerSerializer,
    ProductSerializer,
    # FeatureSerializer,
    # ReviewSerializer,
    OrderSerializer,
    OrderItemSerializer,
    # WishlistSerializer,
    GenerateOTPSerializer
)
from django.utils.crypto import get_random_string
from twilio.rest import Client
from django.core.cache import cache
from datetime import datetime, timedelta
from random import randint
from django.db.models import Q

from django.core.mail import send_mail
from django.conf import settings




@api_view(['POST'])
def customer_registration_view(request):
    if request.method == 'POST':
        serializer = CustomerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            name = serializer.validated_data['name']
            phone_number = serializer.validated_data['phone_number']
            password = request.data['password']

            # # Check if the email is already registered
            # if User.objects.filter(username=email).exists():
            #     return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Check if the email or phone number is already registered
            if User.objects.filter(Q(username=email) | Q(customer__phone_number=phone_number)).exists():
                return Response({'error': 'User with this email or phone number already exists.'}, status=status.HTTP_400_BAD_REQUEST)


            # Generate and send OTP
            otp = generate_otp()
            # Code to send OTP via SMS or email

            # Store the OTP and customer data in cache
            otp_expiration = datetime.now() + timedelta(minutes=5)  # Set OTP expiration time
            customer_data = {
                'name': name,
                'email': email,
                'phone_number': phone_number,
                'password': password,
                'otp': otp,
                'otp_expiration': otp_expiration,
            }
            cache.set(email, customer_data)
            if email:
                send_verification_email(email, otp)
            if phone_number:
             # Code to send OTP via SMS
                send_verification_otp(phone_number, otp)
    

            # Return the OTP to the client for verification
            return Response({'otp': otp}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def otp_verification_view(request):
    if request.method == 'POST':
        otp = request.data.get('otp')
        email = request.data.get('email')
        print(email,'-----------------------------email')
        print(otp,'--------------------------otp')

        # Retrieve the stored customer data and OTP from cache
        customer_data = cache.get(email)

        print(customer_data,"............................")
        # otp == customer_data.get('otp')
        # print(otp,"oooooooooooooooooooooooooooooo")


        if customer_data is not None:
            stored_otp = customer_data.get('otp')
            print(stored_otp,'---------------------------')
            otp_expiration = customer_data.get('otp_expiration')

            if otp and stored_otp and otp == stored_otp and datetime.now() <= otp_expiration:
                # Check if the email is already registered
                if User.objects.filter(username=email).exists():
                    return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
            # Create the user
            user = User.objects.create_user(
                username=email,
                email=email,
                password=customer_data['password']
            )

            # Create the customer and save customer data to the database
            customer = Customer.objects.create(
                user=user,
                name=customer_data['name'],
                email=email,
                phone_number=customer_data['phone_number'],
            )

            # Clear the temporary data from cache
            cache.delete(email)



            return Response({'message': 'Customer registered successfully'}, status=status.HTTP_201_CREATED)

        return Response({'error': 'Invalid or expired OTP'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def generate_otp_view(request):
    if request.method == 'POST':
        serializer = GenerateOTPSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            phone_number = serializer.validated_data.get('phone_number')

            try:
                customer = None
                otp = generate_otp()

                if email:
                    customer = Customer.objects.get(email=email)
                    # if customer.is_verified:
                    #     return Response({'detail': 'Customer is already verified.'}, status=status.HTTP_400_BAD_REQUEST)
                    customer.otp = otp
                    customer.save()
                    send_verification_email(email, otp)

                elif phone_number:
                    customer = Customer.objects.get(phone_number=phone_number)
                    # if customer.is_verified:
                    #     return Response({'detail': 'Customer is already verified.'}, status=status.HTTP_400_BAD_REQUEST)
                    customer.otp = otp
                    customer.save()
                    send_verification_otp(phone_number, otp)

                if customer:
                    return Response({'message': 'OTP sent successfully', 'otp': otp}, status=status.HTTP_200_OK)
                else:
                    return Response({'detail': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)

            except Customer.DoesNotExist:
                return Response({'detail': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def customer_login_view(request):
    if request.method == 'POST':
        serializer = CustomerLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            phone_number = serializer.validated_data.get('phone_number')
            otp = serializer.validated_data.get('otp')

            customer = None
            if email:
                try:
                    customer = Customer.objects.get(email=email)
                except Customer.DoesNotExist:
                    return Response({'detail': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)
            elif phone_number:
                try:
                    customer = Customer.objects.get(phone_number=phone_number)
                except Customer.DoesNotExist:
                    return Response({'detail': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)
            
            if customer:
                # if not customer.is_verified:
                    if otp == customer.otp:
                        customer.is_verified = True
                        customer.save()
                    else:
                        return Response({'detail': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

                    user = customer.user
                    login(request, user)
                    refresh = RefreshToken.for_user(user)
                    return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)




def send_verification_email(email, otp):
    subject = 'Email Verification OTP'
    message = f'Your OTP for email verification is: {otp}'
    from_email = 'sahunisha.bluethink@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


def send_verification_otp(phone_number, otp):
        # Initialize the Twilio client with your account SID and auth token
        client = Client("AC9124c9f9d6ebad6bffa281e0d3604bb4","1e6de29e7dc0429b161c0f1a7de5cd86")

        # Set up the message details
        from_number = "+16073604837"
        to_number = phone_number
        message = f"Your OTP for phone number verification is: {otp}"

        # Send the SMS
        client.messages.create(from_=from_number, body=message, to=to_number)


def generate_otp():
    return get_random_string(length=4, allowed_chars='1234567890')


# @api_view(['POST'])
# def customer_registration_view(request):
#     if request.method == 'POST':
#         serializer = CustomerRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             name = serializer.validated_data['name']
#             phone_number = serializer.validated_data['phone_number']

#             if User.objects.filter(username=email).exists():
#                 return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

#             user = User.objects.create_user(
#                 username=email,
#                 email=email,
#                 password=request.data['password']
#             )
#             customer = Customer.objects.create(
#                 user=user,
#                 name=name,
#                 email=email,
#                 phone_number=phone_number
#             )
#             # otp = customer.send_verification_email()
#             # customer.otp=otp
#             # customer.save()

#             # return Response({'otp': otp}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# @api_view(['POST'])
# def customer_login_view(request):
#     if request.method == 'POST':
#         serializer = CustomerLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             password = serializer.validated_data['password']
#             otp = serializer.validated_data['otp']
#             print(otp,"uuuuuuuuuuuuuuuuuuuu")

#             user = authenticate(request, username=email, password=password)
#             if user is not None:
#                 customer = Customer.objects.get(user=user)
#                 print(customer,"lllllllllllllllllll")
                
#                 if not customer.is_verified:
#                     print("yyyyyyyyyyyyyyyyyyy")
#                     if otp == customer.otp: 
#                         customer.is_verified = True
#                         customer.save()
#                         print(customer.otp,"pppppppppppppppppppppp")
#                     else:
#                         return Response({'detail': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

#                 login(request, user)
#                 refresh = RefreshToken.for_user(user)
#                 return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)

#         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def customer_logout_view(request):
    if request.method == 'POST':
        logout(request)
        return Response({'message': 'Logout Successfully'},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def customer_detail_view(request):
    if request.method == 'GET':
        customer = request.user.customer
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        customer = request.user.customer
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def customer_list_create_view(request):
#     if request.method == 'GET':
#         customers = Customer.objects.all()
#         serializer = CustomerSerializer(customers, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             user = User.objects.create_user(
#                 username=serializer.validated_data['email'],
#                 email=serializer.validated_data['email'],
#                 password=request.data['password']
#             )
#             customer = Customer.objects.create(
#                 user=user,
#                 name=serializer.validated_data['name'],
#                 email=serializer.validated_data['email'],
#                 phone_number=serializer.validated_data['phone_number']
#             )
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def customer_detail_api_view(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def product_list_create_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def feature_list_create_view(request):
#     if request.method == 'GET':
#         features = Feature.objects.all()
#         serializer = FeatureSerializer(features, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = FeatureSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def feature_detail_api_view(request, pk):
#     try:
#         feature = Feature.objects.get(pk=pk)
#     except Feature.DoesNotExist:
#         raise Http404

#     if request.method == 'GET':
#         serializer = FeatureSerializer(feature)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = FeatureSerializer(feature, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         feature.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def review_list_create_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, pk):
#     try:
#         review = Review.objects.get(pk=pk)
#     except Review.DoesNotExist:
#         raise Http404

#     if request.method == 'GET':
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ReviewSerializer(review, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def order_list_create_view(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def order_detail_api_view(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def order_item_list_create_view(request):
    if request.method == 'GET':
        order_items = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def order_item_detail_api_view(request, pk):
    try:
        order_item = OrderItem.objects.get(pk=pk)
    except OrderItem.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderItemSerializer(order_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def wishlist_list_create_view(request):
#     if request.method == 'GET':
#         wishlists = Wishlist.objects.all()
#         serializer = WishlistSerializer(wishlists, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = WishlistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def wishlist_detail_api_view(request, pk):
#     try:
#         wishlist = Wishlist.objects.get(pk=pk)
#     except Wishlist.DoesNotExist:
#         raise Http404

#     if request.method == 'GET':
#         serializer = WishlistSerializer(wishlist)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = WishlistSerializer(wishlist, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         wishlist.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
