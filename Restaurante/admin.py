from django.contrib import admin
from .models import Restaurante
# Register your models here.
@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nombre','Direccion')