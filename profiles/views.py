from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import AddressForm
from .models import Address
from .utils import getAddresses

# Create your views here.
@login_required
def profile(request):
    profile = get_object_or_404(User, pk=request.user.id)
    addresses = getAddresses(request)
    context = {
        'profile': profile,
        'addresses': addresses,
        }
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
    
    return render(request, 'profiles/address-form.html', context)
