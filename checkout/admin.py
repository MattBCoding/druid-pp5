from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = (
                       'order_number',
                       'date',
                       'delivery_cost',
                       'order_total',
                       'grand_total',
                       'original_bag',
                       'stripe_pid'
                       )

    fields = (
              'order_number',
              'user_profile',
              'full_name',
              'email',
              'phone_number',
              'street_address_1',
              'street_address_2',
              'town_or_city',
              'county',
              'postcode',
              'country',
              'date',
              'delivery_cost',
              'order_total',
              'grand_total',
              'original_bag',
              'stripe_pid',
              'order_status'
              )

    list_display = (
                    'order_number',
                    'date',
                    'full_name',
                    'order_total',
                    'delivery_cost',
                    'grand_total',
                    'order_status'
                    )

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
