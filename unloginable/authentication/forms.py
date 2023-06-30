from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'code')


class LoginForm(forms.Form):
    """this is a buggy form, i know!"""
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=12, widget=forms.PasswordInput)

