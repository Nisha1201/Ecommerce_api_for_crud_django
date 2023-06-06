from rest_framework import serializers
from .models import Category, Customer, Products, Order ,Cart,CartItem,CustomerProfile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['id','fullname', 'first_name', 'last_name', 'phone', 'email', 'password']

    def get_first_name(self, obj):
        print(obj,'.....................')
        names = obj.fullname.split()
        print(names,'---------------------')
        print(len(names),',,,,,,,,,,,,,,,,,,,')
        if len(names) > 0:
            return names[0]
        return ""

    def get_last_name(self, obj):
        names = obj.fullname.split()
        print(names[1:],'nnnnnnnnnnnnnn')
        if len(names) > 1:
            return ' '.join(names[1:])
        
        return ""
    # class Meta:
    #     model = Customer
    #     fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True,)
    class Meta:
        model = Products
        fields = ['name','price','category','description','image']
        # fields = '__all__'


# class OrderSerializer(serializers.HyperlinkedModelSerializer):
#     product = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
#     customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
#     class Meta:
#         model = Order
#         fields = ['id','url', 'product', 'customer', 'quantity', 'price', 'address', 'phone', 'date', 'status']



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    cartitem_set = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'cartitem_set']


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ['id','customer','fullname', 'phone', 'email', 'password']