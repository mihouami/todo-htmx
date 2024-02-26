from .models import User, Country, Car
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all())  # Provide queryset for country
    cars = forms.ModelMultipleChoiceField(queryset=Car.objects.all())  # Provide queryset for cars
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'cars', 'country')