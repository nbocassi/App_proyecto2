from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre=models.CharField(max_length=120)
    apellido=models.CharField(max_length=120)
    email=models.EmailField()
    pass

class Profesor(models.Model):
    nombre=models.CharField(max_length=120)
    apellido=models.CharField(max_length=120)
    email=models.EmailField()
    profesion=models.CharField(max_length=120)
    pass

class Curso(models.Model):
    nombre=models.CharField(max_length=120)
    comision=models.IntegerField()
    pass

class Entregable(models.Model):
    nombre=models.CharField(max_length=120)
    fecha_de_entrega=models.DateField()
    entregado=models.BooleanField()
    pass