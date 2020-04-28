from Montaje.models import Montaje
from rest_framework import serializers

class MontajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Montaje
        fields = ('id', 'Titulo', 'Descripcion')