from django.db import models

class EntrevistasModel(models.Model):
    Titulo = models.CharField(max_length=100)
    Localidad = models.CharField(max_length=100)
    Entrevistado = models.CharField(max_length=100)
    Anecdota = models.TextField()
    Corresponsal = models.CharField(max_length=100)
    Finalizado = models.DateField(auto_now_add=True)


# Create your models here.
