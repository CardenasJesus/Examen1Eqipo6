from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import UserE, Task
from ToDo import models
from .forms import NewTaskForm, NewUserForm, UpdateTaskForm, UpdateUserForm

# Create your views here.
def Empleados(request):
    user = UserE.objects.all()
    return render(request,'empleados.html',{"user": user})

class DeleteUser(generic.DeleteView):
    template_name = "empleados_delete.html"
    model = models.UserE
    success_url = reverse_lazy("empleados")

def Tareas(request):
    task = Task.objects.all()
    return render(request,'tareas.html',{'tarea': task})

class CreateTask (generic.CreateView):
    template_name = "tareas_create.html"
    model = models.Task
    form_class = NewTaskForm
    success_url = reverse_lazy("tareas")
    

class CreateUser (generic.CreateView):
    template_name = 'empleados_create.html'
    model = models.UserE
    form_class = NewUserForm
    success_url = reverse_lazy("empleados")

class UpdateUser(generic.UpdateView):
    template_name = "empleados_update.html"
    model = models.UserE
    form_class = UpdateUserForm
    success_url = reverse_lazy("empleados")

class UpdateTask(generic.UpdateView):
    template_name = "tareas_update.html"
    model = models.Task
    form_class = UpdateTaskForm
    success_url = reverse_lazy("tareas")

class DeleteTask(generic.DeleteView):
    template_name = "tareas_delete.html"
    model = models.Task
    success_url = reverse_lazy("tareas")
