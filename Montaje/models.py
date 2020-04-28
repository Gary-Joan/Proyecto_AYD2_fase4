from django.db import models

# Create your models here.
class Montaje(models.Model):
    Titulo = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=100, default = "")

    def __str__(self):             
        return self.Titulo