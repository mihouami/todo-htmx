from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['description', 'user', 'is_completed', 'added_at', 'updated_at']

# Register your models here.
admin.site.register(Todo, TodoAdmin)