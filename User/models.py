from django.db import models
# Imports para modelo User
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    cui = models.CharField(max_length=15)
    nombre_completo = models.CharField(max_length=100)
    numero_telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_completo