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
    title = models.CharField(max_length=128, null=False, blank=False)
    slug = models.SlugField(max_length=128, unique=True)
    category = models.ForeignKey(BlogCategory, null=False, blank=False, on_delete=models.SET_DEFAULT, default=1)
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.SET_DEFAULT, default=1)
    created_on = models.DateField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:
            if slugify(self.title) != self.slug:
                self.slug = slugify(self.title)
        else:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)
