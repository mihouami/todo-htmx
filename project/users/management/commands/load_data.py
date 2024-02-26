import csv
from django.core.management import BaseCommand
from django.conf import settings
from users.models import Car, Country

class Command(BaseCommand):
    help = 'load data to Car and countries tables'
    
    def handle(self, *args, **kwargs):
        cars_file = settings.BASE_DIR/'users'/'data'/'cars.csv'
        countries_file = settings.BASE_DIR/'users'/'data'/'countries.csv'

        with open(cars_file) as file:
            reader = csv.reader(file)
            for row in reader:
                Car.objects.get_or_create(manufacturer=row[0], country=row[1])
        
        with open(countries_file) as file:
            reader = csv.reader(file)
            for row in reader:
                Country.objects.get_or_create(name=row[3])