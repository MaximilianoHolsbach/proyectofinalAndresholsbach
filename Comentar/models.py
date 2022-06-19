from operator import truediv
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from Entrevistas.models import EntrevistasModel

class ComentarModel(models.Model):
    Titulo = models.ForeignKey(EntrevistasModel, on_delete=models.CASCADE,)
    Nombre = models.CharField(max_length=100)
    Comentario = models.TextField()
    Email = models.EmailField()



# Create your models here.
