from django import forms

from .models import Menu, Menu_Ingrediente

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('Nombre', 'Descripcion', 'Precio')

class MenuIngredienteForm(forms.ModelForm):

    class Meta:
        model = Menu_Ingrediente
        fields = ('Menu', 'Ingrediente', 'Disponible', 'Cantidad', 'Dimensional')