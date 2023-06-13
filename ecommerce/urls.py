# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #     path('categories/', views.category_list),
# #     path('categories/<int:pk>/', views.category_detail),
# #     path('customers/', views.customer_list),
# #     path('customers/<int:pk>/', views.customer_detail,name='customer-detail'),
# #     path('products/', views.products_list),
# #     path('products/<int:pk>/', views.products_detail,name='products-detail'),
# #     path('orders/', views.order_list),
# #     path('orders/<int:pk>/', views.order_detail,name='order-detail'),

# #     path('carts/', views.cart_list, name='cart-list'),
# #     path('carts/<int:pk>/', views.cart_detail, name='cart-detail'),
# #     path('cartitems/', views.cartitem_list, name='cartitem-list'),
# #     path('cartitems/<int:pk>/', views.cartitem_detail, name='cartitem-detail'),

# #     path('registration/', views.registration, name='customer-registration'),
# #     path('login/', views.login, name='customer-login'),
# #     path('logout/', views.logout, name='customer-logout'),

# # ]



# from django.urls import path
# from . import views


# urlpatterns = [

#     path('register/', views.customer_register, name='customer_registration'),
#     path('login/', views.customer_login, name='customer_login'),
#     path('logout/', views.customer_logout, name='customer_logout'),

#     # URL patterns for CustomerProfile views
#     path('profiles/', views.customer_profile_view, name='customer-profiles'),
#     path('profiles/<int:pk>/', views.customer_profile_detail_view, name='customer-profile-detail'),

#     # URL patterns for Category views
#     path('categories/', views.category_list, name='categories'),
#     path('categories/<int:pk>/', views.category_detail, name='category-detail'),

#     # URL patterns for Products views
#     path('products/', views.products_list, name='products'),
#     path('products/<int:pk>/', views.products_detail, name='products-detail'),

#     # URL patterns for Order views
#     path('orders/', views.order_list, name='orders'),
#     path('orders/<int:pk>/', views.order_detail, name='order-detail'),

#     # URL patterns for Cart views
#     path('carts/', views.cart_list, name='carts'),
#     path('carts/<int:pk>/', views.cart_detail, name='cart-detail'),

#     # URL patterns for CartItem views
#     path('cartitems/', views.cart_item_list, name='cart-items'),
#     path('cartitems/<int:pk>/', views.cart_item_detail, name='cart-item-detail'),

#     path('wishlist/',views.wishlist_list, name='wishlist-list'),
#     path('wishlist/<int:pk>/', views.wishlist_detail, name='wishlist-detail'),
# ]



from django.urls import path
from . import views
urlpatterns = [
    # path('register/', views.customer_registration_view, name='customer-registration'),
    # path('login/', views.customer_login_view, name='customer-login'),
    path('logout/', views.customer_logout_view, name='customer-logout'),

    # path('cust/detail/', views.customer_detail_view, name='customer-detail'),
    # path('cust/list/', views.customer_list_create_view, name='customer-list'),
    path('cust/detail/<int:pk>/', views.customer_detail_api_view, name='customer-detail-api'),

    path('pro/list/', views.product_list_create_view, name='product-list'),
    path('pro/detail/<int:pk>/', views.product_detail_api_view, name='product-detail-api'),

    # path('fea/list/', views.feature_list_create_view, name='feature-list'),
    # path('fea/detail/<int:pk>/', views.feature_detail_api_view, name='feature-detail-api'),

    # path('rev/list/', views.review_list_create_view, name='review-list'),
    # path('rev/detail/<int:pk>/', views.review_detail_api_view, name='review-detail-api'),

    path('order/list/', views.order_list_create_view, name='order-list'),
    path('order/detail/<int:pk>/', views.order_detail_api_view, name='order-detail-api'),

    path('ord-item/list/', views.order_item_list_create_view, name='order-item-list'),
    path('ord-item/detail/<int:pk>/', views.order_item_detail_api_view, name='order-item-detail-api'),

    # path('wishlist/list/', views.wishlist_list_create_view, name='wishlist-list'),
    # path('wishlist/detail/<int:pk>/', views.wishlist_detail_api_view, name='wishlist-detail-api'),

    # path('register/',views.customer_registration_view, name='customer-registration'),
    path('generate-otp/',views.generate_otp_view, name='generate-otp'),
    path('login/',views.customer_login_view, name='customer-login'),

     path('register/', views.customer_registration_view, name='customer-registration'),
    path('verify-otp/', views.otp_verification_view, name='otp-verification'),
]
