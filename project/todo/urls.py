from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('complete/<int:pk>/', complete, name='complete'),
]