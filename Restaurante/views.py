from rest_framework.views import APIView, View
from rest_framework.response import Response
from django.shortcuts import render
from .models import Restaurante
from .serializers import RestauranteSerializer
from rest_framework import status
from .forms import RestauranteForm
from silk.profiling.profiler import silk_profile
from silk.profiling.profiler import silk_meta_profiler

def login(request):
    return render(request, 'login.html', {})

# Create your views here.

class RestauranteView(APIView):
    permission_classes = []
    @silk_profile(name="Restaurante get")
    def get(self, request):
        id = request.data['Restaurante']
        queryset = Restaurante.objects.get(id=id)
        serializer = RestauranteSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

    @silk_profile(name="Restaurante post")
    def post(self, request):
        nombre = request.data['Nombre']
        direccion = request.data['Direccion']
        queryset = Restaurante(Nombre = nombre, Direccion = direccion)
        queryset.save()
        serializer = RestauranteSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

class DeleteRestauranteView(APIView):
    permission_classes = []

    def post(self, request):
        id = request.data['Restaurante']
        queryset = Restaurante.objects.get(id=request.GET.get('DeleteButton'))
        queryset.delete()
        return Response(status=status.HTTP_200_OK)

def RestauranteNewView(request):
    if request.method == "POST":
        form = RestauranteForm(request.POST)
        if form.is_valid():
            restaurante = form.save(commit=False)
            restaurante.save()
    form = RestauranteForm()
    return render(request, 'restaurante_new.html', {'form': form})

def RestauranteSimpleView(request):
    queryset = Restaurante.objects.all()
    return render(request, 'restaurante.html', {'object_list':queryset})