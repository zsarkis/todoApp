from django.contrib.auth.models import User
from django import forms
from django.core import validators
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
from django.contrib.auth.models import User


def username_present(username):
    if User.objects.filter(username=username).exists():
        return True

    return False


class RegisterForm(forms.Form):
    user = forms.CharField()  # request.POST['user']
    email = forms.EmailField()  # request.POST['email']
    passw = forms.CharField(widget=forms.PasswordInput())  # request.POST['psw']
    passwCheck = forms.CharField(widget=forms.PasswordInput())  # request.POST['psw-repeat']

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get("user")
        email = cleaned_data.get("email")
        passw = cleaned_data.get("passw")
        passwCheck = cleaned_data.get("passwCheck")

        if email is not None:
            if username_present(user):
                raise forms.ValidationError('Please try another username.', code='username taken')
            elif passw != passwCheck:
                raise forms.ValidationError('Passwords must match.', code='password mismatch')
            else:
                User.objects.create_user(user, email, passw)
