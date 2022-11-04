
from django.db import models
from django.forms import PasswordInput

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30) 

