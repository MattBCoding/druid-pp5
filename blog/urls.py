from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add-post/', views.addBlogPost, name='add_blog_post'),
    path('edit-post/<slug:slug>/', views.editBlogPost, name='edit_blog_post'),
    path('delete-blog-post/<str:pk>/', views.deleteBlogPost, name='delete_blog_post'),
    path('<slug:slug>/', views.blogPostDetail, name='blog_post_detail'),
    path('htmx/get-categories/', views.getCategories, name='get_categories'),
    path('htmx/add-category/', views.addBlogCategory, name='add_blog_category'),
    path('htmx/add-blog-category-container/', views.getAddBlogCategoryContainer, name='get_add_blog_category_container'),
    path('htmx/edit-category/<str:pk>/', views.editBlogCategory, name='edit_blog_category'),
    path('htmx/get-blog-category-detail/<str:pk>/', views.getBlogCategoryDetail, name='get_blog_category_detail'),
    path('htmx/delete-category/<str:pk>/', views.deleteBlogCategory, name='delete_blog_category'),
    path('htmx/get-delete-blog-category/<str:pk>/', views.getDeleteBlogCategory, name='get_delete_blog_category'),
]