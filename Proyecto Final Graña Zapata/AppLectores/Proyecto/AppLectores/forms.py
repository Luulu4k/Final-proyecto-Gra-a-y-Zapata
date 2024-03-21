from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EscritorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    nacionalidad = forms.CharField(max_length=100)
    genero_preferido = forms.CharField(max_length=50)

class LibroForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    autor = forms.CharField(max_length=100)
    genero = forms.CharField(max_length=50)
    

class LectorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    genero = forms.CharField(max_length=50)
    preferencias_genero_literario = forms.CharField(max_length=100)
    
class RegistroUsuario(UserCreationForm):

    class Meta: 

        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]



class EditarUsuario(UserChangeForm):

    password= None

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]



class AvatarFormulario(forms.Form):

    imagen = forms.ImageField()

