from django.contrib import admin
from .models import BlogPost, BlogCategory
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class BlogPostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogCategory)
