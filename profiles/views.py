from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AddressForm, DeleteUserForm, EditUserForm
from .models import Address
from .utils import getAddresses
from products.models import Product

User = get_user_model()


@login_required
def profile(request):
    profile = get_object_or_404(User, pk=request.user.id)
    addresses = getAddresses(request)
    form = DeleteUserForm()
    context = {
        'profile': profile,
        'addresses': addresses,
        'form': form,
        }
    if request.method == 'POST':
        address_id = request.POST.get('address')
        if request.user.address.filter(default__exact=True).exists():
            currentDefaultAddress = get_object_or_404(
                                                      Address,
                                                      user=request.user,
                                                      default=True)
            currentDefaultAddress.default = False
            currentDefaultAddress.save(update_fields=['default'])
        updateDefaultAddress = get_object_or_404(
                                                 Address,
                                                 user=request.user,
                                                 id=address_id)
        updateDefaultAddress.default = True
        updateDefaultAddress.save(update_fields=['default'])
    return render(request, 'profiles/profile.html', context)


@login_required
def addAddress(request):
    profile = get_object_or_404(User, pk=request.user.id)
    form = AddressForm(request.POST or None)
    context = {
        'form': form,
        'profile': profile
        }
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = profile
            # check to see if a default address exists before save
            if request.user.address.filter(default__exact=True).exists():
                # change previous default address default field to false
                if address.default is True:
                    defaultAddress = get_object_or_404(
                                                       Address,
                                                       user=request.user,
                                                       default=True)
                    defaultAddress.default = False
                    defaultAddress.save(update_fields=['default'])
                    # save new address once old one has been updated
                    address.save()
                else:
                    address.save()
            else:
                address.default = True
                address.save()
            messages.success(request, 'Your address has been successfully \
                                updated')
            return redirect('profile')

    return render(request, 'profiles/address_form.html', context)


@login_required
def editAddress(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.user == address.user:
        if request.method == 'POST':
            form = AddressForm(request.POST, instance=address)
            if form.is_valid():
                if form.data.get('default', False):
                    defaultAddress = get_object_or_404(
                                                       Address,
                                                       user=request.user,
                                                       default=True)
                    if address != defaultAddress:
                        defaultAddress.default = False
                        defaultAddress.save(update_fields=['default'])
                form.save()
                return redirect('profile')
        else:
            form = AddressForm(instance=address)
            context = {
                'form': form,
                'address': address,
            }
            return render(request, 'profiles/address_form.html', context)
    else:
        return redirect('home')


@login_required
def deleteAddress(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if address.user == request.user:
        address.delete()
        return redirect('profile')


@login_required
def deleteUserAccount(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user == user:
        if request.method == 'POST':
            form = DeleteUserForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['email'] == user.email:
                    user = request.user
                    logout(request)
                    user.delete()
                    messages.success(request, 'Your account has been deleted')
                    return redirect('home')
                else:
                    messages.error(request, 'Your email address is incorrect')
            else:
                messages.error(request, 'Please enter your email address')


@login_required
def editUserAccount(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user == user:
        form = EditUserForm(instance=user)
        context = {'form': form}
        if request.method == 'POST':
            form = EditUserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your details have been updated')
                return redirect('profile')

        return render(request, 'profiles/edit_user_form.html', context)
    else:
        messages.error(request, 'Error - \
            you can not access that users account')
        return redirect('profile')


@login_required
def favourite(request, pk):
    '''
    View to add or remove user to product favourite list
    '''
    product = get_object_or_404(Product, pk=pk)
    slug = product.slug
    # favourite = False
    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
        # favourite = False
    else:
        product.favourites.add(request.user)
        # favourite = True
    if request.htmx:
        context = {
            'product': product,
            # 'favourite': favourite
        }
        return render(request, 'products/snippets/favourite.html', context)
    # handle update from my wishlist page
    if request.method == 'POST':
        products = Product.objects.filter(favourites=request.user)
        context = {
            'products': products,
            # 'favourite': favourite
        }
        return render(request, 'profiles/my_favourites.html', context)

    return HttpResponseRedirect(reverse('product_detail', args=[slug]))


@login_required
def my_favourites(request):
    '''
    View to handle user requests to view their product wishlist
    '''
    products = Product.objects.all().filter(favourites=request.user)
    context = {
        'products': products,
    }
    return render(request, 'profiles/my_favourites.html', context)
