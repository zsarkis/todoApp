from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

# Create your views here.

def todoView(request):
    allTodoItems = TodoItem.objects.all()
    return render(request, 'todo.html',
                  {'all_items': allTodoItems})

def addTodo(request):
    content = request.POST['content']
    new_item = TodoItem(content= content)
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item = TodoItem.objects.get(id= todo_id)
    item.delete()
    return HttpResponseRedirect('/todo/')

def clear(request):
    for item in TodoItem.objects.all():
        item.delete()
    return HttpResponseRedirect('/todo/')
