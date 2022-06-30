from dataclasses import fields
from django import forms
from .models import Category, Product, Review, Response
from django_summernote.widgets import SummernoteWidget
from blog.widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    '''
    form to add a product to the database
    '''
    class Meta:
        model = Product
        exclude = ('slug', 'favourites',)
        widgets = {
            'description': SummernoteWidget(),
            'highlights': SummernoteWidget(),
            'technical_details': SummernoteWidget(),
        }

    primary_image = forms.ImageField(
        label='Primary Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        names = [(c.id, c.friendly_name) for c in categories]
        self.fields['category'].choices = names


class ReviewForm(forms.ModelForm):
    '''
    Form for customers to add a review of a product they have purchased
    '''
    class Meta:
        model = Review
        fields = {
            'title',
            'review',
            'rating',
        }
        field_order = {
            'title',
            'review',
            'rating'
        }


class ResponseForm(forms.ModelForm):
    '''
    Form for employees to add a response to a customer review
    '''
    class Meta:
        model = Response
        fields = {
            'response',
        }
        widgets = {
            'response': SummernoteWidget(),
        }
