from re import S
from django import forms
from .models import Category, Product 
from django_summernote.widgets import SummernoteWidget
from blog.widgets import CustomClearableFileInput

class ProductForm(forms.ModelForm):
    '''
    form to add a product to the database
    '''
    class Meta:
        model = Product
        exclude = ('slug',)
        widgets = {
            'description': SummernoteWidget(),
            'highlights': SummernoteWidget(),
            'technical_details': SummernoteWidget(),
        }
    
    primary_image = forms.ImageField(label='Primary Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        names = [(c.id, c.friendly_name) for c in categories]
        self.fields['category'].choices = names
