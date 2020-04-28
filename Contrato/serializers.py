from Contrato.models import Contrato, Contrato_Menu
from Ingrediente.serializers import IngredienteSerializer
from Menu.serializers import MenuSerializer
from Montaje.serializers import MontajeSerializer
from Restaurante.serializers import RestauranteSerializer
from Salon.serializers import SalonSerializer
from User.serializers import UserSerializer
from rest_framework import serializers


class ContratoMenuSerializer(serializers.ModelSerializer):
    Menu = MenuSerializer(read_only=True)

    class Meta:
        model = Contrato_Menu
        fields = ('id', 'Menu')
        
class ContratoSerializer(serializers.ModelSerializer):
    Cliente = UserSerializer(read_only=True)
    Gerente = UserSerializer(read_only=True)
    Menu = ContratoMenuSerializer(read_only=True)
    Montaje = MontajeSerializer(read_only=True)
    Restaurante = RestauranteSerializer(read_only=True)
    Salon = SalonSerializer(read_only=True)

    class Meta:
        model = Contrato
        fields = ('id', 'Cliente', 'Gerente', 'Menu', 'Montaje', 'Restaurante', 'Salon')