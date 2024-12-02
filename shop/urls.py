from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_view, name='products_list'),
    path('products/add/', views.add_product_view, name='add_product'),
    path('categories/add/', views.add_category_view, name='add_category'),
    path('products/<int:pk>/', views.product_details_view, name='product_details'),
]
