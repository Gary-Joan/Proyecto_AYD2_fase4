from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Contrato
from .serializers import ContratoSerializer
from rest_framework import status

from Ingrediente.models import Ingrediente
from Menu.models import Menu
from Montaje.models import Montaje
from Restaurante.models import Restaurante
from Salon.models import Salon
from User.models import User
from .forms import ContratoForm

# Create your views here.
class ContratoView(APIView):
    permission_classes = []

    def get(self, request):
        id = request.data['Contrato']
        queryset = Contrato.objects.get(id=id)
        serializer = ContratoSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        cliente = request.data['Cliente']
        gerente = request.data['Gerente']
        menu = request.data['Menu']
        montaje = request.data['Montaje']
        restaurante = request.data['Restaurante']
        salon = request.data['Salon']

        cliente = User.objects.get(id=cliente)
        gerente = User.objects.get(id=gerente)
        menu = Menu.objects.get(id=menu)
        montaje = Montaje.objects.get(id=montaje)
        restaurante = Restaurante.objects.get(id=restaurante)
        salon = Salon.objects.get(id=salon)
        
        queryset = Contrato(Cliente= cliente, Gerente = gerente, Menu=menu, Montaje=montaje, Restaurante=restaurante, Salon=salon)
        queryset.save()
        serializer = ContratoSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

class DeleteContratoView(APIView):
    permission_classes = []

    def post(self, request):
        id = request.data['Ingrediente']
        queryset = Ingrediente.objects.get(id=id)
        queryset.delete()
        return Response(status=status.HTTP_200_OK)

def ContratoNewView(request):
    if request.method == "POST":
        form = ContratoForm(request.POST)
        if form.is_valid():
            contrato = form.save(commit=False)
            contrato.save()
    form = ContratoForm()
    queryset = Contrato.objects.filter()
    return render(request, 'contrato.html', {'form': form,'object_list':queryset})

def ContratoSimpleView(request):
    queryset = Contrato.objects.filter()
    return render(request, 'contrato.html', {'form': form,'object_list':queryset})
