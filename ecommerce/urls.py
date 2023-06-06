# from django.urls import path
# from . import views

# urlpatterns = [
#     path('categories/', views.category_list),
#     path('categories/<int:pk>/', views.category_detail),
#     path('customers/', views.customer_list),
#     path('customers/<int:pk>/', views.customer_detail,name='customer-detail'),
#     path('products/', views.products_list),
#     path('products/<int:pk>/', views.products_detail,name='products-detail'),
#     path('orders/', views.order_list),
#     path('orders/<int:pk>/', views.order_detail,name='order-detail'),

#     path('carts/', views.cart_list, name='cart-list'),
#     path('carts/<int:pk>/', views.cart_detail, name='cart-detail'),
#     path('cartitems/', views.cartitem_list, name='cartitem-list'),
#     path('cartitems/<int:pk>/', views.cartitem_detail, name='cartitem-detail'),

#     path('registration/', views.registration, name='customer-registration'),
#     path('login/', views.login, name='customer-login'),
#     path('logout/', views.logout, name='customer-logout'),

# ]



from django.urls import path
from . import views


urlpatterns = [

    path('register/', views.customer_register, name='customer_registration'),
    path('login/', views.customer_login, name='customer_login'),
    path('logout/', views.customer_logout, name='customer_logout'),

    # URL patterns for CustomerProfile views
    path('profiles/', views.customer_profile_view, name='customer-profiles'),
    path('profiles/<int:pk>/', views.customer_profile_detail_view, name='customer-profile-detail'),

    # URL patterns for Category views
    path('categories/', views.category_list, name='categories'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),

    # URL patterns for Products views
    path('products/', views.products_list, name='products'),
    path('products/<int:pk>/', views.products_detail, name='products-detail'),

    # URL patterns for Order views
    path('orders/', views.order_list, name='orders'),
    path('orders/<int:pk>/', views.order_detail, name='order-detail'),

    # URL patterns for Cart views
    path('carts/', views.cart_list, name='carts'),
    path('carts/<int:pk>/', views.cart_detail, name='cart-detail'),

    # URL patterns for CartItem views
    path('cartitems/', views.cart_item_list, name='cart-items'),
    path('cartitems/<int:pk>/', views.cart_item_detail, name='cart-item-detail'),
]