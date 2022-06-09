from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout
from django.contrib import messages
from .forms import AddressForm, DeleteUserForm, EditUserForm
from .models import Address
from .utils import getAddresses

User = get_user_model()
# Create your views here.
@login_required
def profile(request):
    profile = get_object_or_404(User, pk=request.user.id)
    addresses = getAddresses(request)
    form = DeleteUserForm(request.POST or None)
    context = {
        'profile': profile,
        'addresses': addresses,
        'form': form,
        }
    if request.method == 'POST':
        address_id = request.POST.get('address')
        if request.user.address.filter(default__exact=True).exists():
            currentDefaultAddress = get_object_or_404(Address, user=request.user, default=True)
            currentDefaultAddress.default = False
            currentDefaultAddress.save(update_fields=['default'])
        updateDefaultAddress = get_object_or_404(Address, user=request.user, id=address_id)
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
                if address.default == True:
                    currentDefaultAddress = get_object_or_404(Address, user=request.user, default=True)
                    currentDefaultAddress.default = False
                    currentDefaultAddress.save(update_fields=['default'])
                    # save new address once old one has been updated
                    address.save()
                else:
                    address.save()
            else:
                address.default = True
                address.save()
            # insert confirmation message to user confirming address saved successfully
            return redirect('profile')
    
    return render(request, 'profiles/address_form.html', context)

@login_required
def editAddress(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.user == address.user:
        if request.method == 'POST':
            form = AddressForm(request.POST, instance=address)
            if form.is_valid():
                print('form is valid')
                if form.data.get('default', False):
                    print('data equals true')
                    currentDefaultAddress = get_object_or_404(Address, user=request.user, default=True)
                    print('got previous default address')
                    if address != currentDefaultAddress:
                        print('there is another address that is default')
                        currentDefaultAddress.default = False
                        currentDefaultAddress.save(update_fields=['default'])
                        print('other address removed as default')
                form.save()
                print('form saved')
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
        messages.error(request, 'Error - you can not access that users account')
        return redirect('profile')
