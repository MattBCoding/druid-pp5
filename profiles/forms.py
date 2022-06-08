from django import forms
from .models import Address
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
        # self.helper = FormHelper()
        # self.helper.layout = Layout(
        #     FloatingField(
        #         'street_address_1',
        #         'street_address_2',
        #         'town_or_city',
        #         'county',
        #         'postcode',
        #         'phone_number',
        #         'default'),
        #         ButtonHolder(
        #             Submit('submit', 'Submit',)
        #         )


        # )
        placeholders = {
            'street_address_1': 'Street Address Line 1',
            'street_address_2': 'Street Address Line 2',
            'town_or_city': 'Town or City',
            'county': 'County, State or Province',
            'postcode': 'Postal Code or Zip Code',
            'phone_number': 'Phone Number',
            'default': 'Set as default address',
        }

        self.fields['street_address_1'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'


class DeleteUserForm(forms.Form):
    email = forms.EmailField()