from Ingrediente.models import Ingrediente
from rest_framework import serializers

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'Nombre', 'Descripcion')