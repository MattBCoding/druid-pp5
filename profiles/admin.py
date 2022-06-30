from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Address, User

# Register your models here.
admin.site.register(Address)
admin.site.register(User)
