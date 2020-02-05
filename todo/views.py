from django.contrib.auth.decorators import login_required
from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .user import RegisterForm, username_present

from .models import TodoItem
from django.contrib.auth.models import User


# Create your views here.

def todoView(request):
    allTodoItems = TodoItem.objects.filter(user_id=request.user.id)
    return render(request, 'todo.html',
                  {'all_items': allTodoItems})


@login_required
def addTodo(request):
    content = request.POST['content']
    new_item = TodoItem(content=content, user_id=request.user.id)
    new_item.save()
    return HttpResponseRedirect('/todo/')


@login_required
def deleteTodo(request, todo_id):
    item = TodoItem.objects.get(id=todo_id)
    item.delete()
    return HttpResponseRedirect('/todo/')


@login_required
def clear(request):
    for item in TodoItem.objects.filter(user_id=request.user.id):
        item.delete()
    return HttpResponseRedirect('/todo/')


def callRegister(request):
    if request.method == 'POST':
        register = RegisterForm(request.POST)
        if register.is_valid():
            user = register.cleaned_data['user']
            email = register.cleaned_data['email']
            passw = register.cleaned_data['passw']
            passwCheck = register.cleaned_data['passwCheck']
            return HttpResponseRedirect('/login/')

    else:
        register = RegisterForm(initial={'user':'','email':'','passw':'','passwCheck':''})

    return render(request, 'register.html',
                  {'register': register})
