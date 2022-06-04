from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    ''' Adds custom fields to the signup form
        used by allauth for user registration'''
    first_name = forms.CharField(max_length=50, label='First Name', required=True)
    last_name = forms.CharField(max_length=50, label='Last Name', required=True)
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
