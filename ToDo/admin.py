from django.contrib import admin

# Register your models here.
from ToDo import models

@admin.register(models.Task)
class Tasks(admin.ModelAdmin):
    list_display = ["nombre", "descripcion", "status"]

@admin.register(models.UserE)
class Users(admin.ModelAdmin):
    list_display = ['nombre', 'apellidoP', 'apellidoM', 'password', 'status']
