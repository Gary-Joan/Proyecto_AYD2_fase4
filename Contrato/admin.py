from django.contrib import admin
from .models import Contrato

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ( 'Cliente','Gerente', 'Montaje', 'Restaurante', 'Salon')