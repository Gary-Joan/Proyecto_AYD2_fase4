from django.db import models

# Create your models here.
class Salon(models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=100, default = "")
    Capacidad = models.IntegerField(default=0)

    def __str__(self):             
        return self.Nombre