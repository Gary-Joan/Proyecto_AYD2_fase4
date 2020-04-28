from django.db import models

# Create your models here.
class Restaurante(models.Model):
    Nombre = models.CharField(max_length=50, unique=True)
    Direccion = models.CharField(max_length=100)

    def __str__(self):             
        return self.Nombre