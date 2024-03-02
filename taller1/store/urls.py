# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_product, name='create_product'),
    path('success/', views.success_created, name='success_created'),
    path('list/', views.list_products, name='list_products'),
    path('view/<int:product_id>/', views.view_product, name='view_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]


