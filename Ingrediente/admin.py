from django.contrib import admin
from .models import Ingrediente
# Register your models here.
@admin.register(Ingrediente)

class ingredienteAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Descripcion')
