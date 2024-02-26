from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages

# Create your views here.
def register(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            messages.success(request, 'User registered with success')
            form.save()
        else:
            messages.warning(request, 'Something went wrong')
    context = {'form':form}
    return render(request, 'register.html', context)
