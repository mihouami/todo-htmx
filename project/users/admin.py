from django.contrib import admin
from .models import Car, Country, User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'country']  # Add any additional fields you want to display in the list view
    add_fieldsets = (
            (
                None,
                {
                    'classes': ('wide',),
                    'fields': ('email', 'cars', 'country', 'password1', 'password2'),
                },
            ),
        )

# Register your models here.
admin.site.register(Car)
admin.site.register(Country)
admin.site.register(User, CustomUserAdmin)


