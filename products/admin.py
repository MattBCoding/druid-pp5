from django.contrib import admin
from .models import Product, Category, Image, Review, Response
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', 'highlights', 'technical_details',)
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'primary_image',
        'is_active',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(Review)
admin.site.register(Response)
