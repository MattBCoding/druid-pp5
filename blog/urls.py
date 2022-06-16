from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add-post/', views.addBlogPost, name='add_blog_post'),
    path('edit-post/<slug:slug>/', views.editBlogPost, name='edit_blog_post'),
    path('delete-blog-post/<str:pk>/', views.deleteBlogPost, name='delete_blog_post'),
    path('<slug:slug>/', views.blogPostDetail, name='blog_post_detail'),
    path('htmx/get-categories/', views.getCategories, name='get_categories'),
]