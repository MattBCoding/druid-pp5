from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('add_address/', views.addAddress, name='add_address'),
]