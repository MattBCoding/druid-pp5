from allauth.account.forms import SignupForm
from django import forms
from .models import ContactMessage


class CustomSignupForm(SignupForm):
    ''' Adds custom fields to the signup form
        used by allauth for user registration'''
    first_name = forms.CharField(max_length=50,
                                 label='First Name',
                                 required=True)
    last_name = forms.CharField(max_length=50,
                                label='Last Name',
                                required=True)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class ContactMessageForm(forms.ModelForm):
    '''
    Form for customers to submit messages to contact the company
    '''
    class Meta:
        model = ContactMessage
        fields = (
            'email',
            'subject',
            'message',
        )

    def __init__(self, *args, **kwargs):
        '''
        Add placeholders and classes to the form,
        remove auto-generated labels,
        set auto focus on first field
        '''
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'example@youremail.com',
            'subject': 'The topic of your message',
            'message': 'The details of your message',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
