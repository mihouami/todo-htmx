from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User


#from django.contrib.auth import get_user_model
#User = get_user_model()



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



def login_user(request):
    if not request.user.is_authenticated:
        form = LoginForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You have been logged in')
                    return redirect('login')
        context = {'form':form}
        return render(request, 'login.html', context)
    else:
        return redirect('register')
    
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')


