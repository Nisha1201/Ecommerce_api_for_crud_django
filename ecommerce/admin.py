from django.contrib import admin

from django.contrib import admin
from .models import Products,Category, Customer, Order,Cart,CartItem,CustomerProfile,CustomerManager



# 1
class CustomerAdmin(admin.ModelAdmin):
    # list_display = ['id','first_name','last_name','phone','email','password']
    #  list_display = ['id','full_name','phone','email','password']
    list_display = ['id','fullname','phone','email','password','is_active','is_staff']
admin.site.register(Customer,CustomerAdmin)

# 2
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Category,CategoryAdmin)


# 3
class AdminProduct(admin.ModelAdmin):
    # list_display = ['id','name', 'price', 'category','description']
    list_display = ['id','name', 'price', 'category','description','image']
admin.site.register(Products,AdminProduct)



# 4
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','product','customer','quantity','price','address','phone','date','status']
admin.site.register(Order,OrderAdmin)

# 5
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user','created_at']
admin.site.register(Cart,CartAdmin)


# 6
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id','product','cart','quantity','price_ht']
admin.site.register(CartItem,CartItemAdmin)

# 7
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ['id','customer','fullname','phone','email','password']
    # list_display = ['fullname','phone','email','password']
admin.site.register(CustomerProfile,CustomerProfileAdmin)



