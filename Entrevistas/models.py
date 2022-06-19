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
    Imagen = models.ImageField(upload_to="Fotos/", null=True, blank=True)
    Corresponsal = models.ForeignKey(User, on_delete=models.CASCADE)
    Finalizado = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Titulo


# Create your models here.
