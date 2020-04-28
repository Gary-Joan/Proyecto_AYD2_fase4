from Restaurante.models import Restaurante
from rest_framework import serializers

#Serializador para creacion de usuario, utilizando username, email, password
class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ('id', 'Nombre', 'Direccion')