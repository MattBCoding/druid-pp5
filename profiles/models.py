from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    street_address_1 = models.CharField(max_length=80, null=False, blank=False)
    street_address_2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=False, blank=False, default='IE')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name_plural = 'Addresses'
