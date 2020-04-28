from django import forms

from .models import Montaje

class MontajeForm(forms.ModelForm):

    class Meta:
        model = Montaje
        fields = ('Titulo', 'Descripcion',)