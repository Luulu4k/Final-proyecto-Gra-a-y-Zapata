from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Escritor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    genero_preferido = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    
    def __str__(self):
        return self.titulo

class Lector(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.CharField(max_length=50)
    preferencias_genero_literario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete= models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null = True, blank= True)
    