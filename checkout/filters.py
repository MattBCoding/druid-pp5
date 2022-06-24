import django_filters
from .models import Order
from django import forms
from django.db import models

class OrderFilter(django_filters.FilterSet):
    '''
    Filter for the Order model to aid searching
    '''
    class Meta:
        model = Order
        fields = {
            'order_number': ['icontains'],
            'user_profile': ['exact'],
            'date': ['range'],
            'order_status': ['exact'],
        }

    @classmethod
    def filter_for_lookup(cls, field, lookup_type):
        if isinstance(field, models.DateField) and lookup_type == 'range':
            return django_filters.DateRangeFilter, {}

        return super().filter_for_lookup(field, lookup_type)


class HelpfulFilterSet(django_filters.FilterSet):
    @classmethod
    def filter_for_field(cls, f, name, lookup_expr):
        filter = super(HelpfulFilterSet, cls).filter_for_field(f, name, lookup_expr)
        filter.extra['help_text'] = f.help_text
        return filter


class UserOrderFilter(django_filters.FilterSet):
    '''
    Filter for users to filter their orders
    '''
    class Meta:
        model = Order
        fields = {
            'order_number': ['icontains'],
            'date': ['range'],
            'order_status': ['exact'],
        }

    @classmethod
    def filter_for_lookup(cls, field, lookup_type):
        if isinstance(field, models.DateField) and lookup_type == 'range':
            return django_filters.DateRangeFilter, {}

        return super().filter_for_lookup(field, lookup_type)
