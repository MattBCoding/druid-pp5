from django import forms
from .models import BlogCategory, BlogPost
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput


class BlogCategoryForm(forms.ModelForm):
    '''
    form to add categories for blog posts
    '''
    class Meta:
        model = BlogCategory
        fields = ('name',)


class BlogPostForm(forms.ModelForm):
    '''
    form to add blog posts
    '''
    class Meta:
        model = BlogPost
        fields = (
            'title',
            'category',
            'image_url',
            'image',
            'content',
        )
        widgets = {
            'content': SummernoteWidget(),
        }

    image = forms.ImageField(
                             label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = BlogCategory.objects.all()
        names = [(c.id, c.name) for c in categories]

        self.fields['category'].choices = names
