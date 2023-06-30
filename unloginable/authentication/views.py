from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, SignUpForm


def index(request):
    """some people call it home :)"""
    if request.method == 'GET':
        user = request.user
        return render(request, 'authentication/index.html', {'user': user})


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'authentication/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('/auth/')

        # either form not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'authentication/index.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                return render(request, 'authentication/index.html')
            else:
                print("user is not authenticated")
            return redirect('/auth/index/')
    else:
        form = SignUpForm()
    return render(request, 'authentication/signup.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('/auth/')
