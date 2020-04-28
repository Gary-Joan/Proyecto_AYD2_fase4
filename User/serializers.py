from User.models import User
from rest_framework import serializers

#Serializador para creacion de usuario, utilizando username, email, password
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'nombre_completo', 'cui', 'numero_telefono')