from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    dirección = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class proveedor (models.Model):
    razon_social = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    rep_legal = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    dirección = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
        
    def __str__(self):
        return self.nombre

# class Usuario(AbstractUser):
#     fecha_nacimiento = models.DateField(blank=True, null=True)

