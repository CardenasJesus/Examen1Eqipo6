from django import forms
from .models import Task, UserE

class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "nombre",
            "descripcion",
            "status",
            "UserE"
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"type":"text","class":"form-control"}),
            "descripcion": forms.Textarea(attrs={"rows":3,"type":"text","class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "UserE_id": forms.Select(attrs={"type":"select","class":"formcontrol"})
        }
    
class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "nombre",
            "descripcion",
            "status",
            "UserE"
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"type":"text","class":"form-control"}),
            "descripcion": forms.Textarea(attrs={"rows":3,"type":"text","class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "UserE_id": forms.Select(attrs={"type":"select","class":"formcontrol"})
        }

class NewUserForm(forms.ModelForm):
    class Meta:
        model = UserE
        fields = [
            "nombre",
            "apellidoP",
            "apellidoM",
            "password",
            "status"
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Nombre"}),
            "apellidoP": forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Apellido paterno"}),
            "apellidoM": forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Apellido materno"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Contraseña"}),
        }

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = UserE
        fields = [
            "nombre",
            "apellidoP",
            "apellidoM",
            "password",
            "status"
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Nombre"}),
            "apellidoP": forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Apellido paterno"}),
            "apellidoM": forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Apellido materno"}),
        }