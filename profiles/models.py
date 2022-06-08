from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django_countries.fields import CountryField
from django.conf import settings


'''
custom user model and usermanager adapted from tutorial by Justin Mitchel
available at
www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model/
'''
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        '''
        Creates and saves a User with the given email and password
        '''
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, password, first_name, last_name):
        '''
        Creates and saves a staff user with the given email and password
        '''
        user = self.create_user(email,
                                first_name,
                                last_name,
                                password=password,
                                )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        '''
        Creates and saves a superuser with the given email and password
        '''
        user = self.create_user(email,
                                first_name,
                                last_name,
                                password=password,
                                )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


User = settings.AUTH_USER_MODEL
class Address(models.Model):
    user = models.ForeignKey(
                             User,
                             on_delete=models.CASCADE,
                             related_name='address')
    street_address_1 = models.CharField(
                                        max_length=80,
                                        null=False,
                                        blank=False
                                        )
    street_address_2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(
                           blank_label='Country',
                           null=False,
                           blank=False,
                           default='IE'
                           )
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name_plural = 'Addresses'


class User(AbstractBaseUser):
    objects = UserManager()
    email = models.EmailField(
                              verbose_name='email address',
                              max_length=255,
                              unique=True
                              )
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin


