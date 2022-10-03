from asyncio import create_task
from venv import create
from django.urls import  path
from .views import create_tasks, list_tasks, delete_tasks

urlpatterns = [
    path('', list_tasks),
    path('new/', create_tasks, name='create_tasks'),
    path('delete_tasks/<int:task_id>/', delete_tasks, name='delete_tasks')
]