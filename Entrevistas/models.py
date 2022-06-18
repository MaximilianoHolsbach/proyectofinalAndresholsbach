from operator import truediv
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class EntrevistasModel(models.Model):
    Titulo = models.CharField(max_length=100)
    Localidad = models.CharField(max_length=100)
    Entrevistado = models.CharField(max_length=100)
    Anecdota = models.TextField()
    Corresponsal = models.ForeignKey(User, on_delete=models.CASCADE)
    Finalizado = models.DateField(auto_now_add=True)


# Create your models here.
