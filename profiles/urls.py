from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('add_address/', views.addAddress, name='add_address'),
    path('edit_address/<str:pk>/', views.editAddress, name='edit_address'),
    path('delete_address/<str:pk>/', views.deleteAddress, name='delete_address'),
    path('delete_account/<str:pk>/', views.deleteUserAccount, name='delete_user_account'),
    path('edit_account/<str:pk>/', views.editUserAccount, name='edit_user_account'),
    path('favourite/<str:pk>/', views.favourite, name='favourite'),
]