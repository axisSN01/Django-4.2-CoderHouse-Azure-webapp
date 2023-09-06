from django.db import models
import pdb
# Create your models here.
from django.contrib.auth.models import User

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40, null=True)  
    comision = models.IntegerField()
    

    def is_odd(self):
        if self.id%2 != 0:
            return True
        
        return False

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, default="")
    
