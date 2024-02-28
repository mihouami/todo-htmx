from .models import Todo
from django import forms

class TodoForm(forms.ModelForm):
    description = forms.TextInput()
      
    class Meta:
        model = Todo
        exclude = ["user"]
    
    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['description'].label = ''
        self.fields['importance'].label = ''


class TodoFilterForm(forms.Form):
    todo = forms.CharField()