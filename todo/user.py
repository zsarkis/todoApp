from django.contrib.auth.models import User
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    user = request.POST['user']
    email = request.POST['email']
    passw = request.POST['psw']
    passwCheck = request.POST['psw-repeat']
    if passw != passwCheck:
        return HttpResponseRedirect('/register/')

    user = User.objects.create_user(user, email, passw)

    return HttpResponseRedirect('/login/')
