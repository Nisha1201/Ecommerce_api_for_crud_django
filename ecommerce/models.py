# from django.db import models
# import datetime
# from django.utils import timezone
# # FOR AUTHENTICATION PURPOSE:
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin


# class CustomerManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
        
#         email = self.normalize_email(email)


#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)


# class Customer(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     fullname = models.CharField(max_length=100)
#     phone = models.CharField(max_length=10)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomerManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['fullname']

#     def __str__(self):
#         return self.email


# class CustomerProfile(models.Model):
#     customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
#     fullname = models.CharField(max_length=100)  
#     phone = models.CharField(max_length=10)
#     email=models.EmailField()
#     password = models.CharField(max_length=100)
#     def __str__(self):
#         return f"{self.fullname}"

#     objects = CustomerManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['full_name']

#     def __str__(self):
#         return f"{self.full_name}"


# class Category(models.Model):
#     name= models.CharField(max_length=50)
#     def __str__(self):
#         return self.name
    
# class Products(models.Model):
#     name = models.CharField(max_length=60)
#     price= models.IntegerField(default=0)
#     category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
#     description= models.CharField(max_length=250, default='', blank=True, null= True)
#     image = models.ImageField(upload_to='product_images/')
#     # cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.name



# class Order(models.Model):
#     product = models.ForeignKey(Products,
#                                 on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer,
#                                  on_delete=models.CASCADE)                           
#     quantity = models.IntegerField(default=1)
#     price = models.IntegerField()
#     address = models.CharField (max_length=50, default='', blank=True)
#     phone = models.CharField (max_length=50, default='', blank=True)
#     date = models.DateField (default=datetime.datetime.today)
#     status = models.BooleanField (default=False)
#     def __str__(self):
#         return f"{self.product} - {self.customer}"
    



# class Cart(models.Model):
#     user = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     # created_at = models.DateTimeField(default=datetime.date.today)
#     created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return str(self.user)

# class CartItem(models.Model):
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     price = models.FloatField(blank=True)
#     cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
# def __str__(self):
#         return  str(self.product)


# class Wishlist(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.customer} - {self.product}"





# Another one:
from django.db import models
from django.contrib.auth.models import User
# from django.utils.timezone import now
# from django.core.mail import send_mail
# from django.utils.crypto import get_random_string
# from twilio.rest import Client

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    
 
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to="images", default="")
    feature = models.CharField(max_length=1000, null=True, blank=True)
 
    def __str__(self):
        return self.name
 
 
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100)
 
    def __str__(self):
        return str(self.id)
 
    @property 
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
 
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
 
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return str(self.order)
 
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
 
# class CheckoutDetail(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     phone_number = models.CharField(max_length=10, blank=True, null=True)
#     total_amount = models.CharField(max_length=10, blank=True,null=True)
#     address = models.CharField(max_length=300)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zipcode = models.CharField(max_length=100)
#     date_added = models.DateTimeField(auto_now_add=True)
 
#     def __str__(self):
#         return self.address
    


# class Wishlist(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product)

#     def __str__(self):
#         return f"{self.customer.name}'s Wishlist"


# class Feature(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     feature = models.CharField(max_length=1000, null=True, blank=True)
 
#     def __str__(self):
#         return str(self.product) + " Feature: " + self.feature
 
# class Review(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     content = models.TextField()
#     datetime = models.DateTimeField(default=now)
    #  def __str__(self)    #       return str(self.customer) +  " Review: " + self.content                                                   