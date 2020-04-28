from django import forms

from .models import Salon

class SalonForm(forms.ModelForm):

    class Meta:
        model = Salon
        fields = ('Nombre', 'Descripcion', 'Capacidad',)