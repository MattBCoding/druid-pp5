from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('management/', views.product_management, name='product_management'),
]