from django.db import models
from django.conf import settings
from django.utils.text import slugify


User = settings.AUTH_USER_MODEL

# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    '''
    need to add save override to prevent featured_products
    being saved initially, model instance needs to be saved first
    then the relationship can be added to the model
    see https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_many/
    '''
    title = models.CharField(max_length=128, null=False, blank=False)
    slug = models.SlugField(max_length=128, unique=True)
    category = models.ForeignKey(BlogCategory, null=False, blank=False, on_delete=models.SET_DEFAULT, default=1)
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.SET_DEFAULT, default=1)
    created_on = models.DateField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    # featured_products = models.ManyToManyField(Product, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)
