from operator import is_
from django.shortcuts import render
from .models import Product, Category
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def all_products(request):
    '''
    products home page
    contains all available products
    '''
    # only return active products
    products = Product.objects.all().filter(is_active=True)
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)

@staff_member_required
def product_management(request):
    '''
    View to access product management page
    and options for product management
    '''
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request, 'products/product_management.html', context)

