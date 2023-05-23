from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list),
    path('categories/<int:pk>/', views.category_detail),
    path('customers/', views.customer_list),
    path('customers/<int:pk>/', views.customer_detail),
    path('products/', views.products_list),
    path('products/<int:pk>/', views.products_detail),
    path('orders/', views.order_list),
    path('orders/<int:pk>/', views.order_detail),
]