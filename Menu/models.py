from django.db import models
from Ingrediente.models import Ingrediente

# Create your models here.
class Menu(models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=100, default = "")
    Ingredientes = models.ManyToManyField(Ingrediente, through='Menu_Ingrediente')
    Precio = models.IntegerField(default=1)

    def __str__(self):             
        return self.Nombre


class Menu_Ingrediente(models.Model):
    Menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='Menu')
    Ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE, related_name='Ingrediente')
    Disponible = models.BooleanField(default=True)
    Cantidad = models.IntegerField(default=1)
    Dimensional = models.CharField(max_length=50)