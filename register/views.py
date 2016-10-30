from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        if data['password'] == data['confirm_password']:
            user = User.objects.create_user(data['username'], data['email'], data[
                                            'password'], first_name=data['first_name'], last_name=data['last_name'])
            return redirect('/')
        else:
            form.add_error(None, "Passwords don't match!")
            return render(request, 'register/register.html', {'form': form})
    return render(request, 'register/register.html', {'form': form})


def login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        user = authenticate(
            username=data['username'], password=data['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            form.add_error(None, "Username or password is incorrect!")
            return render(request, 'register/login.html', {'form': form})
    return render(request, 'register/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('/')
