# from rest_framework import serializers
# from .models import Category, Customer, Products, Order ,Cart,CartItem,CustomerProfile,Wishlist
# from rest_framework.validators import UniqueValidator

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
#         extra_kwargs = {
#             'name': {
#                 'validators': [UniqueValidator(queryset=Category.objects.all(), message='Category with this name already exists.')]
#             }
#         }


# class CustomerSerializer(serializers.ModelSerializer):
#     first_name = serializers.SerializerMethodField()
#     last_name = serializers.SerializerMethodField()

#     class Meta:
#         model = Customer
#         fields = ['id','fullname', 'first_name', 'last_name', 'phone', 'email', 'password']

#     def get_first_name(self, obj):
#         print(obj,'.....................')
#         names = obj.fullname.split()
#         print(names,'---------------------')
#         print(len(names),',,,,,,,,,,,,,,,,,,,')
#         if len(names) > 0:
#             return names[0]
#         return ""

#     def get_last_name(self, obj):
#         names = obj.fullname.split()
#         print(names[1:],'nnnnnnnnnnnnnn')
#         if len(names) > 1:
#             return ' '.join(names[1:])
        
#         return ""
#     # class Meta:
#     #     model = Customer
#     #     fields = '__all__'


# class ProductSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField(max_length=None, use_url=True,)
#     class Meta:
#         model = Products
#         fields = ['name','price','category','description','image']
#         # fields = '__all__'


# # class OrderSerializer(serializers.HyperlinkedModelSerializer):
# #     product = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
# #     customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
# #     class Meta:
# #         model = Order
# #         fields = ['id','url', 'product', 'customer', 'quantity', 'price', 'address', 'phone', 'date', 'status']



# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'

# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = '__all__'

# class CartSerializer(serializers.ModelSerializer):
#     cartitem_set = CartItemSerializer(many=True, read_only=True)

#     class Meta:
#         model = Cart
#         fields = ['id', 'user', 'created_at', 'cartitem_set']


# class CustomerProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomerProfile
#         fields = ['id','customer','fullname', 'phone', 'email', 'password']


# class WishlistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Wishlist
#         fields = '__all__'




# Another way:
from rest_framework import serializers
from .models import Customer, Product, Order, OrderItem
from django.core.validators import RegexValidator
from rest_framework import serializers

class CustomerRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r'^(\+91|0)?[6789]\d{9}$',
                message="Invalid phone number. Please enter a valid phone number.",
                code='invalid_phone_number'
            )
        ]
    )
    password = serializers.CharField(max_length=128)


class GenerateOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, allow_blank=True)
    phone_number = serializers.CharField(required=False, allow_blank=True,
                                           validators=[
            RegexValidator(
                regex=r'^(\+91|0)?[6789]\d{9}$',
                message="Invalid phone number. Please enter a valid phone number.",
                code='invalid_phone_number'
            )
        ]
                                         )
                  

class CustomerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, allow_blank=True)
    phone_number = serializers.CharField(max_length=15, required=False, allow_blank=True)
    otp = serializers.CharField(max_length=6)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone_number', "is_verified","otp"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image','feature']

# class FeatureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Feature
#         fields = ['id', 'product', 'feature']

# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ['id', 'customer', 'product', 'content', 'datetime']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'date_ordered', 'complete', 'transaction_id']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'order', 'quantity', 'date_added']

# class CheckoutDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CheckoutDetail
#         fields = ['id', 'customer', 'order', 'phone_number', 'total_amount', 'address', 'city', 'state', 'zipcode', 'date_added']