from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem
from django.contrib.auth.models import User


def username_present(username):
    if User.objects.filter(username=username).exists():
        return True

    return False


class RegisterForm(forms.Form):


    def register(request):
        user = request.POST['user']
        email = request.POST['email']
        passw = request.POST['psw']
        passwCheck = request.POST['psw-repeat']
        # if passw != passwCheck:
        #     raise forms.ValidationError(('Invalid value'), code='passwords do not match')
        # if username_present(user):
        #     raise forms.ValidationError(('Invalid value'), code='username taken')

        user = User.objects.create_user(user, email, passw)

        return HttpResponseRedirect('/login/')

