from Salon.models import Salon
from rest_framework import serializers

#Serializador para creacion de usuario, utilizando username, email, password
class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = ('id', 'Nombre', 'Descripcion', 'Capacidad')