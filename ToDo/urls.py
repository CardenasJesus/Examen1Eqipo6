from django.urls import path,include
from .views import Empleados, Tareas,UpdateTask, DeleteUser, CreateTask, DeleteTask,UpdateUser, CreateUser
urlpatterns = [
    path('',Empleados,),
    ##Tasks
    path('tareas/', Tareas, name="tareas"),
    path('updateT/<int:pk>/', UpdateTask.as_view(), name="update"),
    path('createT/', CreateTask.as_view(), name="NewTask"),
    path('deleteT/<int:pk>', DeleteTask.as_view(), name="DeleteTask"),

    ##Users
    path('empleados/', Empleados, name="empleados"),
    path('updateE/<int:pk>/', UpdateUser.as_view(), name="updateUser"),
    path('createE/', CreateUser.as_view(), name="NewUser"),
    path('deleteE/<int:pk>', DeleteUser.as_view(), name="DeleteUser"),
]