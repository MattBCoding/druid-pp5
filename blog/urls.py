from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add-post/<str:pk>/', views.addBlogPost, name='add_blog_post'),
    
]