from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse, Http404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm, OrderStatusForm
from checkout.models import Order, OrderLineItem
from products.models import Product
from bag.contexts import bag_contents
from profiles.utils import getAddresses
from profiles.models import Address
from profiles.forms import AddressForm
from .filters import OrderFilter, UserOrderFilter
import stripe
import json

User = get_user_model()

# Create your views here.
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address_1': request.POST['street_address_1'],
            'street_address_2': request.POST['street_address_2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],             
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        'One of the products in your bag was not found in our \
                            database. Please contact us for assistance!'
                    ))
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, 'There are no items in your bag at the moment.')
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = get_object_or_404(User, pk=request.user.id)
                if 'address_id' in request.GET:
                    address = Address.objects.get(pk=request.GET['address_id'])
                    order_form = OrderForm(initial={
                        'full_name': profile.get_full_name(),
                        'email': profile.email,
                        'phone_number': address.phone_number,
                        'street_address_1': address.street_address_1,
                        'street_address_2': address.street_address_2,
                        'town_or_city': address.town_or_city,
                        'county': address.county,
                        'postcode': address.postcode,
                        'country': address.country,
                    })
                elif profile.address.filter(default__exact=True).exists():
                    default = get_object_or_404(Address, user=profile, default=True)
                    order_form = OrderForm(initial={
                        'full_name': profile.get_full_name(),
                        'email': profile.email,
                        'phone_number': default.phone_number,
                        'street_address_1': default.street_address_1,
                        'street_address_2': default.street_address_2,
                        'town_or_city': default.town_or_city,
                        'county': default.county,
                        'postcode': default.postcode,
                        'country': default.country,
                    })
                else:
                    order_form = OrderForm(initial={
                        'full_name': profile.get_full_name(),
                        'email': profile.email,                        
                    })
            except Exception:
                order_form = OrderForm()
            if getAddresses(request):
                addresses = getAddresses(request)
            else:
                addresses = False
        else:
            order_form = OrderForm()
            addresses = False
        
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
            'addresses': addresses,
        }

        return render(request, template, context)

def checkout_success(request, order_number):
    '''
    Handles successful checkouts
    '''
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = User.objects.get(pk=request.user.id)
        order.user_profile = profile
        order.save()

        # save the new user address
        if save_info:
            address_data = {
                'street_address_1': order.street_address_1,
                'street_address_2': order.street_address_2,
                'town_or_city': order.town_or_city,
                'county': order.county,
                'postcode': order.postcode,
                'country': order.country,
                'phone_number': order.phone_number,
            }
            address_form = AddressForm(address_data)
            if address_form.is_valid():
                new_address = address_form.save(commit=False)
                new_address.user = profile
                new_address.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}')

    if 'bag' in request.session:
        del request.session['bag']
    
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

@staff_member_required
def order_management(request):
    '''
    Employee view to access order details
    '''
    orders = Order.objects.all()
    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs
    title = 'Order Management'

    template = 'checkout/order_management.html'
    context = {
        'orders': orders,
        'my_filter': my_filter,
        'title': title,
    }
    return render(request, template, context)

@staff_member_required
def update_order_status(request, order_number):
    '''
    A view to handle updates to the order status of a given order
    '''
    order = get_object_or_404(Order, order_number=order_number)
    form = OrderStatusForm(instance=order)

    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order updated successfully.')
            return redirect('order_management')
        else:
            messages.error(request, 'Failed to update order, double check the form')
    
    context = {
        'form': form,
        'order': order,
    }
    template = 'checkout/update_order_status.html'
    return render(request, template, context)

def order_status(request):
    '''
    View to handle requests to view the status of a given order
    '''
    context = {}
    template = 'checkout/get_order_status.html'
    return render(request, template, context)

def order_status_hx(request):
    '''
    View to handle the HX request to retrieve the order status
    '''
    if not request.htmx:
        raise Http404
    try:
        order_number = request.GET.get('order_number').upper()
        order = get_object_or_404(Order, order_number=order_number)
        order_status = order.get_order_status_display
        order_date = order.date
    except:
        order = None
    if order is None:
        return HttpResponse('No order found')
    context = {
        'order_number': order_number,
        'order_status': order_status,
        'order_date': order_date,
    }
    template = 'checkout/snippets/order_status.html'
    return render(request, template, context)

@login_required
def my_orders(request):
    '''
    View for logged in users to access their order history
    '''
    if request.user.is_authenticated:
        orders = Order.objects.all().filter(user_profile=request.user)
        my_filter = UserOrderFilter(request.GET, queryset=orders)
        orders = my_filter.qs
        title = 'My Order History'

    template = 'checkout/order_management.html'
    context = {
        'orders': orders,
        'my_filter': my_filter,
        'title': title,
    }
    return render(request, template, context)
