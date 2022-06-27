from itertools import product
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from checkout.models import OrderLineItem, Order
from .forms import ProductForm, ReviewForm, ResponseForm
from .models import Product, Category, Review, Response


# Create your views here.
User = get_user_model()

def all_products(request):
    '''
    products home page
    contains all available products
    '''
    # only return active products
    products = Product.objects.all().filter(is_active=True)
    query = None

    if request.GET:
        if 'category' in request.GET:
            query = request.GET['category']
            products = products.filter(category__name__icontains=query)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query) |
                       Q(highlights__icontains=query) |
                       Q(technical_details__icontains=query))
            products = products.distinct().filter(queries)

    context = {
        'products': products,
        'search_query': query,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, slug):
    '''
    product detail view for individual products
    '''
    product = get_object_or_404(Product, slug=slug)
    favourite = False
    if product.favourites.filter(id=request.user.id).exists():
        favourite = True
    reviews = Review.objects.all().filter(product=product)
    can_review = False
    # check if user has previously purchased the product
    if request.user.is_authenticated:
        print('user is authenticated')
        user = User.objects.get(email=request.user.email)
        user_orders = [order.id for order in Order.objects.filter(user_profile=user)]
        line_items = OrderLineItem.objects.filter(order__pk__in=user_orders, product__pk=product.id).exists()
        #check if the user has previously written a review
        if line_items:
            print('user has purchased the product')
            can_review = True
            if reviews.filter(author=user).exists():
                print('user has reviewed before')
                can_review = False
        else:
            print('user has not purchased the product')
    else:
        print(request.user)

    review_form = ReviewForm()
    response_form = ResponseForm()
    context = {
        'product': product,
        'favourite': favourite,
        'reviews': reviews,
        'can_review': can_review,
        'review_form': review_form,
        'response_form': response_form,
    }
    return render(request, 'products/product_detail.html', context)

@login_required
def product_review_receiver(request, pk):
    '''
    View to handle a form submission to add or edit a product review
    from a user. User must be logged in and must have purchased the product to
    submit a review. Product detail view should prevent users accessing the form
    without having purchased the product in most instances.
    '''
    form = ReviewForm(request.POST)
    author = request.user
    product = get_object_or_404(Product, pk=pk)
    if Order.objects.filter(
                            user_profile=author,
                            lineitems__product__pk=pk
                            ):
        if form.is_valid():
            review = form.save(commit=False)
            review.author = author
            print(review.author)
            review.product = product
            print(review.product)
            review.save()
            messages.success(
                            request,
                            'Product review has been added successfully.\n'
                            'Thank you for your feedback.'
                            )
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(
                           request,
                           'Something went wrong. \n'
                           'Please double check your form.')
    else:
        messages.error(
                       request,
                       'You need to have purchased the product to provide a review')

@login_required
def hx_get_edit_review_form(request, pk):
    '''
    View to return the edit review form
    '''
    review = get_object_or_404(Review, pk=pk)
    form = ReviewForm(request.POST or None, instance=review)
    context = {'form': form, 'review': review}
    return render(request, 'products/snippets/edit_product_review.html', context)

@staff_member_required
def hx_get_edit_response_form(request, pk):
    '''
    View to return the edit response form
    '''
    response = get_object_or_404(Response, pk=pk)
    review = get_object_or_404(Review, pk=response.review.id)
    form = ResponseForm(request.POST or None, instance=response)
    context = {
        'form': form,
        'response': response,
        'review_response': review
        }
    return render(request, 'products/snippets/review_response_form.html', context)

@login_required
def update_review_receiver(request, pk):
    '''
    View to receive update review form
    '''
    review = get_object_or_404(Review, pk=pk)
    product = get_object_or_404(Product, pk=review.product.id)
    author = request.user
    if request.method == 'POST':
        if review.author == author:
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                messages.success(request, 'Review successfully updated')
                return redirect(reverse('product_detail', args=[product.slug]))
            else:
                messages.error(request, 'There is a problem with your review submission. Please check the form and try again.')
        else:
            messages.error(request, 'Only the original author of the review can edit it')
            return redirect(reverse('product_detail', args=[product.slug]))
    else:
        messages.error(request, 'Something went wrong, please try again')
        return redirect(reverse('product_detail', args=[product.slug]))

@staff_member_required
def review_response_receiver(request, pk):
    '''
    View to receive employee responses to user reviews
    '''
    review = get_object_or_404(Review, pk=pk)
    product = get_object_or_404(Product, pk=review.product.id)
    employee = request.user
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.author = employee
            response.review = review
            response.save()
            messages.success(request, 'Response recorded successfully')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(request, 'There is something wrong with the form')
            return redirect(reverse('product_detail', args=[product.slug]))
    else:
        messages.error(request, 'Something went wrong, please try again')
        return redirect(reverse('product_detail', args=[product.slug]))

@staff_member_required
def edit_response_receiver(request, pk):
    '''
    View to handle response edit submissions
    '''
    response = get_object_or_404(Response, pk=pk)
    review = get_object_or_404(Review, pk=response.review.id)
    product = get_object_or_404(Product, pk=review.product.id)
    if request.method == 'POST':
        form = ResponseForm(request.POST, instance=response)
        if form.is_valid():
            edit_response = form.save(commit=False)
            edit_response.author = request.user
            edit_response.save()
            messages.success(request, 'Response successfully edited')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(request, 'There is something wrong with the form')
            return redirect(reverse('product_detail', args=[product.slug]))
    else:
        messages.error(request, 'Something went wrong, please try again')
        return redirect(reverse('product_detail', args=[product.slug]))

@login_required
def hx_get_delete_modal(request, pk):
    '''
    View to return the contents for the delete review modal
    '''
    review = get_object_or_404(Review, pk=pk)
    author = request.user
    staff = request.user.is_staff
    if request.htmx:
        if review.author == author or staff:
            context = {
                'delete_review': review,
            }
            return render(request, 'products/snippets/delete_review_modal.html', context)
        else:
            raise Http404
    else:
        raise Http404

@login_required
def delete_review(request, pk):
    '''
    View to handle delete review requests
    '''
    review = get_object_or_404(Review, pk=pk)
    product = get_object_or_404(Product, pk=review.product.id)
    author = request.user
    staff = request.user.is_staff
    if review.author == author or staff:
        review.delete()
        messages.success(request, 'Review successfully deleted')
        return redirect(reverse('product_detail', args=[product.slug]))

    else:
        messages.error(request, 'Only the review author or employees can delete this review.')
        return redirect(reverse('product_detail', args=[product.slug]))


@staff_member_required
def hx_get_response_form(request, pk):
    '''
    View to return the form for employees to respond to customer reviews
    '''
    review = get_object_or_404(Review, pk=pk)
    form = ResponseForm()
    context = {
        'form': form,
        'review_response': review
        }
    return render(request, 'products/snippets/review_response_form.html', context)

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

@staff_member_required
def deactivate_product_modal(request, slug):
    '''
    view to return the product information for the 
    deactivate/activate product modal
    '''
    product = get_object_or_404(Product, slug=slug)
    if request.htmx:
        context = {
            'product': product,
        }
        return render(request, 'products/snippets/product_deactivate_modal.html', context)

@staff_member_required
def deactivate_product(request, slug):
    '''
    view to handle activate or deactivate product requests
    '''
    product = get_object_or_404(Product, slug=slug)
    if request.user.is_staff:
        if product.is_active:
            product.is_active = False
            product.save()
            messages.success(request, 'The product has been deactivated')
            return redirect('product_management')
        else:
            product.is_active = True
            product.save()
            messages.success(request, 'The product has been activated')
            return redirect('product_management')
    else:
        messages.error(request, 'Only employees can change a products activation status')


