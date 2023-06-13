# from django.contrib import admin
# from .models import Products,Category, Customer, Order,Cart,CartItem,CustomerProfile,Wishlist



# # 1
# class CustomerAdmin(admin.ModelAdmin):
#     # list_display = ['id','first_name','last_name','phone','email','password']
#     #  list_display = ['id','full_name','phone','email','password']
#     list_display = ['id','fullname','phone','email','password','is_active','is_staff']
# admin.site.register(Customer,CustomerAdmin)

# # 2
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id','name']
# admin.site.register(Category,CategoryAdmin)


# # 3
# class AdminProduct(admin.ModelAdmin):
#     # list_display = ['id','name', 'price', 'category','description']
#     list_display = ['id','name', 'price', 'category','description','image']
# admin.site.register(Products,AdminProduct)



# # 4
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id','product','customer','quantity','price','address','phone','date','status']
# admin.site.register(Order,OrderAdmin)

# # 5
# class CartAdmin(admin.ModelAdmin):
#     list_display = ['id','user','created_at']
# admin.site.register(Cart,CartAdmin)


# # 6
# class CartItemAdmin(admin.ModelAdmin):
#     list_display = ['id','product','cart','quantity','price']
# admin.site.register(CartItem,CartItemAdmin)

# # 7
# class CustomerProfileAdmin(admin.ModelAdmin):
#     list_display = ['id','customer','fullname','phone','email','password']
#     # list_display = ['fullname','phone','email','password']
# admin.site.register(CustomerProfile,CustomerProfileAdmin)


# # 8
# class WishlistAdmin(admin.ModelAdmin):
#     list_display = ['id','customer','product']
# admin.site.register(Wishlist,WishlistAdmin)


# Another way:________________________
from django.contrib import admin
from .models import Customer, Product,Order, OrderItem

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone_number','is_verified','otp']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'image','feature']

# @admin.register(Feature)
# class FeatureAdmin(admin.ModelAdmin):
#     list_display = ['id', 'product', 'feature']

# @admin.register(Review)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ['id', 'customer', 'product', 'content', 'datetime']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'date_ordered', 'complete', 'transaction_id']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'order', 'quantity', 'date_added']

# @admin.register(CheckoutDetail)
# class CheckoutDetailAdmin(admin.ModelAdmin):
#     list_display = ['id', 'customer', 'order', 'phone_number', 'total_amount', 'address', 'city', 'state', 'zipcode', 'date_added']


# @admin.register(Wishlist)
# class WishlistAdmin(admin.ModelAdmin):
#     list_display = ['id','customer',]