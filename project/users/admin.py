from django.contrib import admin
from .models import Car, Country, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Car)
admin.site.register(Country)
admin.site.register(User, UserAdmin)


