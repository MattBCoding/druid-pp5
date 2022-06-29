from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from requests import post

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import Address
# from profiles.models import UserProfile

import json
import time


User = get_user_model()


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook event from Stripe
        """

        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        print('Username:  ', username)
        if username != 'AnonymousUser':
            print(' WH --- its not an anonymous user')
            profile = User.objects.get(email=username)
            # profile = get_object_or_404(User, pk=self.request.user.id)
            print('Found the users profile')
            print(profile)
            # save the new user address
            if save_info:
                # check to see if the user has addresses saved already
                current = Address.objects.filter(user=profile.id)
                if current:
                    print('CURRENT ADDRESS EXISTS')
                else:
                    print('Getting new address data')
                    sa1 = shipping_details.address.line1
                    sa2 = shipping_details.address.line2
                    toc = shipping_details.address.city
                    county = shipping_details.address.state
                    postcode = shipping_details.address.postal_code
                    country = shipping_details.address.country
                    pn = shipping_details.phone
                    print('creating new address from WH')
                    new = (Address.objects.create('user', profile,
                                                  'street_address_1': sa1,
                                                  'street_address_2': sa2,
                                                  'town_or_city': toc,
                                                  'county': county,
                                                  'postcode': postcode,
                                                  'country': country,
                                                  'phone_number': pn,
                                                  ))
                    print(new)
                    print('New address created')
            # save the new user address
            # if save_info:
            #     print('save info was ticked')
            #     address_data = {
            #         'street_address_1': shipping_details.address.line1,
            #         'street_address_2': shipping_details.address.line2,
            #         'town_or_city': shipping_details.address.city,
            #         'county': shipping_details.address.state,
            #         'postcode': shipping_details.address.postal_code,
            #         'country': shipping_details.address.country,
            #         'phone_number': shipping_details.phone,
            #     }
            #     print('address data is as follows')
            #     print(shipping_details.address.line1)
            #     print(shipping_details.address.line2)
            #     print(shipping_details.address.city)
            #     print(shipping_details.address.state)
            #     print(shipping_details.address.postal_code)
            #     print(shipping_details.address.country)
            #     print(shipping_details.phone)
            #     address_form = AddressForm(address_data)
            #     print('Address Form is as follows:')
            #     print(address_form)
            #     print('checking address form is valid in webhook')
            #     if address_form.is_valid():
            #         print('it is valid in webhook')
            #         address = address_form.save(commit=False)
            #         print('saved but false in webhook')
            #         address.user = profile
            #         print('added user profile to address form in webhook')
            #         if profile.address.filter(default__exact=True).exists():
            #             print('Found a default address for the user')
            #             address.save()
            #         else:
            #             print('no default address found, creating one now')
            #             address.default = True
            #             address.save()
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address_1__iexact=shipping_details.address.line1,
                    street_address_2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} |\
                         SUCCESS: Verified order already in database',
                status=200)
        else:
            print('WH -- ORDER DID NOT EXIST - CREATING ONE FROM WH')
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address_1=shipping_details.address.line1,
                    street_address_2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} |\
                      SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook event from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
