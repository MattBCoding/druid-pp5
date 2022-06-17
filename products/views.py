from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def all_products(request):
    '''
    products home page
    contains all available products
    '''
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
