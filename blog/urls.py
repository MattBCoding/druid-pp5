from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add-post/', views.addBlogPost, name='add_blog_post'),
    path('<slug:slug>/', views.blogPostDetail, name='blog_post_detail'),
    path('edit-post/<slug:slug>/', views.editBlogPost, name='edit_blog_post'),
]