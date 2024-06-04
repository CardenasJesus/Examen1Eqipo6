from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserE(models.Model):
    nombre = models.CharField(max_length=50)
    apellidoP = models.CharField(max_length=30 )
    apellidoM = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    status = models.BooleanField(default='0')
    def __str__(self):
        return self.nombre
    
# Create your models here.
class Task(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    status = models.BooleanField(default='0')
    UserE = models.ForeignKey(UserE, on_delete= models.CASCADE)
    
    
    