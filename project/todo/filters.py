import django_filters
from .models import Todo, User
from django import forms

class TodoFilter(django_filters.FilterSet):
    #prince = django_filters.RangeFilter() 
    added_at = django_filters.DateRangeFilter() #this is working
    #added_at = django_filters.DateFilter(widget=forms.DateInput(attrs={'type':'date'})) #this is not working
    updated_at = django_filters.DateFromToRangeFilter() #this is working
    user = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    importance = django_filters.MultipleChoiceFilter(choices=Todo.ImportanceChoices.choices, widget=forms.CheckboxSelectMultiple())
    

    class Meta:
        model = Todo
        fields = {
            'description':['icontains'], 
            'is_completed':['exact'], 
            #'user__username':['icontains'], 
            #'added_at':['lt','gt'], 
            #'updated_at':['lt','gt'], 
            'importance':['exact'],
        }
