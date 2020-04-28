from django import forms

from .models import Contrato

class ContratoForm(forms.ModelForm):

    class Meta:
        model = Contrato
        fields = ('Cliente', 'Gerente','Menu','Montaje','Restaurante','Salon')