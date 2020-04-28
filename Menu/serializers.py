from Menu.models import Menu, Menu_Ingrediente
from Ingrediente.serializers import IngredienteSerializer
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'Nombre', 'Descripcion', 'Precio')

class MenuIngredienteSerializer(serializers.ModelSerializer):
    Menu = MenuSerializer(read_only=True)
    Ingrediente = IngredienteSerializer(read_only=True)
    class Meta:
        model = Menu_Ingrediente
        fields = ('id', 'Menu', 'Ingrediente', 'Disponible', 'Cantidad', 'Dimensional')
