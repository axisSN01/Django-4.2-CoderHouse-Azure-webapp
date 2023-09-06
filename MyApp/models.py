from django.db import models
import pdb
# Create your models here.
from django.contrib.auth.models import User

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, default="")

class Comision(models.Model):
    cursos = models.ManyToManyField(Curso)

class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default="")
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40, null=True)
    comision = models.ForeignKey(Comision, on_delete=models.SET_NULL, null=True, default="")    

    def is_odd(self):
        if self.id%2 != 0:
            return True
        
        return False
    
