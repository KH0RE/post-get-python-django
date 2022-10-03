from unicodedata import name
from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def list_tasks(request):
    tasks =  Task.objects.all()
    return render(request, 'list_tasks.html', {"tasks": tasks})

def create_tasks(request):
    task = Task(name=request.POST['name'], last_name=request.POST['last_name'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_tasks(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks')