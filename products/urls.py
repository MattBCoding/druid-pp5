from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('management/', views.product_management, name='product_management'),
    path('management/add_product/', views.add_product, name='add_product'),
    path('management/edit_product/<slug:slug>/', views.edit_product, name='edit_product'),
    path('management/deactivate_product/<slug:slug>/', views.deactivate_product, name='deactivate_product'),
    path('management/htmx/deactivate_product_modal/<slug:slug>/', views.deactivate_product_modal, name='deactivate_product_modal'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('reviews/<str:pk>/', views.product_review_receiver, name='product_review_receiver'),
    path('hx/get_update_review_form/<str:pk>/', views.hx_get_edit_review_form, name='get_update_review_form'),
    path('update_review/<str:pk>/', views.update_review_receiver, name='update_review_receiver'),
    path('hx/get_delete_modal/<str:pk>/', views.hx_get_delete_modal, name='get_delete_modal'),
    path('hx/get_response_form/<str:pk>/', views.hx_get_response_form, name='get_response_form'),
    path('hx/get_edit_response_form/<str:pk>/', views.hx_get_edit_response_form, name='get_edit_response_form'),
    path('reviews/response/<str:pk>/', views.review_response_receiver, name='response_receiver'),
    path('reviews/edit_response/<str:pk>/', views.edit_response_receiver, name='edit_response_receiver'),
    path('reviews/delete_review/<str:pk>/', views.delete_review, name='delete_review'),
]