from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Car(models.Model):
    manufacturer = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.manufacturer
    
class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    cars = models.ManyToManyField(Car)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
