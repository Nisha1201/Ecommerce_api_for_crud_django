# from django.urls import path
# from ecommerce import views
# from django.contrib import admin
# urlpatterns = [
#     path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
#     path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
#     path('customers/', views.CustomerListCreateView.as_view(), name='customer-list'),
#     path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),
#     path('products/', views.ProductListCreateView.as_view(), name='product-list'),
#     path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
#     path('orders/', views.OrderListCreateView.as_view(), name='order-list'),
#     path('orders/<int:pk>/', views.OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
#     path('admin/', admin.site.urls),
# ]


# from django.urls import path
# from django.contrib import admin
# from ecommerce.views import (
#     CategoryListCreateView, CategoryRetrieveUpdateDestroyView,
#     CustomerListCreateView, CustomerRetrieveUpdateDestroyView,
#     ProductListCreateView, ProductRetrieveUpdateDestroyView,
#     OrderListCreateView, OrderRetrieveUpdateDestroyView
# )
# from django.conf.urls.static import static
# from django.conf import settings


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('categories/', CategoryListCreateView.as_view(), name='category-list'),
#     path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
#     path('customers/', CustomerListCreateView.as_view(), name='customer-list'),
#     path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),
#     path('products/', ProductListCreateView.as_view(), name='product-list'),
#     path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
#     path('orders/', OrderListCreateView.as_view(), name='order-list'),
#     path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# using fuctions:
from django.urls import path,include
# from ecommerce import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ecommerce.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)