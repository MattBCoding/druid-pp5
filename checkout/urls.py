from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
    path('order_management/update_order_status/<order_number>', views.update_order_status, name='update_order_status'),
    path('order_management/orders/', views.order_management, name='order_management'),
    path('order_status/', views.order_status, name='order_status'),
    path('hx/order_status/', views.order_status_hx, name='order_status_hx'),
    path('my_orders/', views.my_orders, name='my_orders'),
]