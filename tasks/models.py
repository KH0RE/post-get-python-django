from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField(blank=True) #blank=true texto opcional
