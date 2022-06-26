from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.conf import settings


User = settings.AUTH_USER_MODEL

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    highlights = models.TextField(blank=True)
    technical_details = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    primary_image = models.ImageField(null=True, blank=True)
    primary_image_url = models.URLField(max_length=1024, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=254, null=True, blank=True, unique=True)
    is_active = models.BooleanField(
        _("active"), default=True,
        help_text=_(
            "Designates whether this product should be treated as active. "
            "Unselect this instead of deleting products."
        ),
    )
    favourites = models.ManyToManyField(User, blank=True, default=None, related_name='product_favourites')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug:
            if slugify(self.name) != self.slug:
                self.slug = slugify(self.name)
        else:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_favourites(self):
        return self.favourites_set.all()


class Image(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    ONE = 1.0
    TWO = 2.0
    THREE = 3.0
    FOUR = 4.0
    FIVE = 5.0
    RATING_CHOICES = [
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5'),
    ]
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='review')
    author = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL, related_name='product_review')
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, choices=RATING_CHOICES, default=FIVE)
    review = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.title


class Response(models.Model):
    review = models.ForeignKey(Review, null=False, blank=False, on_delete=models.CASCADE, related_name='response')
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.SET_DEFAULT, related_name='response_author', default=1)
    response = models.TextField(blank=False, null=False)
