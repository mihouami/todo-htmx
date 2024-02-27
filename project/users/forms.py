from .models import User, Country, Car
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    country = forms.ModelChoiceField(queryset=Country.objects.order_by('name'))  # Provide queryset for country
    cars = forms.ModelMultipleChoiceField(queryset=Car.objects.all())  # Provide queryset for cars
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'cars', 'country')


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))  
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))  