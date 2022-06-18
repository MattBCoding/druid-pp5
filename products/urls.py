from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('management/', views.product_management, name='product_management'),
    path('management/add_product/', views.add_product, name='add_product'),
    path('management/edit_product/<slug:slug>/', views.edit_product, name='edit_product'),
]