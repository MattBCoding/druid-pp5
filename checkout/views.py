from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from checkout.models import Order

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There are no items in your bag at the moment.')
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)