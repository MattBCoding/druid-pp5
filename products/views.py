from multiprocessing import context
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product, Category

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

@staff_member_required
def add_product(request):
    '''
    view to add a product for employee access only
    '''
    form = ProductForm(request.POST or None, request.FILES or None)
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully')
            return redirect('product_management')
        else:
            messages.error(request, 'There is an error in the form.')

    return render(request, 'products/product_form.html', context)

@staff_member_required
def edit_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES or None, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect('product_management')
        else:
            messages.error(request, 'There is an error in the form.')
    
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'products/product_form.html', context)
