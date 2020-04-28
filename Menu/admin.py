from django.contrib import admin
from .models import Menu ,Menu_Ingrediente
# Register your models here.
@admin.register(Menu)

class menuAdmin(admin.ModelAdmin):
    list_display = ('Menu','Descripcion','Precio')

@admin.register(Menu_Ingrediente)

class menuIngAdmin(admin.ModelAdmin):
    list_display = ('Ingrediente','Disponible','Cantidad')