from django import forms
from .models import Address, User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        '''
        Add placeholders and classes to the form,
        remove auto-generated labels,
        set auto focus on first field
        '''
        super().__init__(*args, **kwargs)
        placeholders = {
            'street_address_1': 'Street Address Line 1',
            'street_address_2': 'Street Address Line 2',
            'town_or_city': 'Town or City',
            'county': 'County, State or Province',
            'postcode': 'Postal Code or Zip Code',
            'phone_number': 'Phone Number',
        }

        self.fields['street_address_1'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country' and field != 'default':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'


class DeleteUserForm(forms.Form):
    email = forms.EmailField()


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
