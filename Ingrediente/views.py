from rest_framework.views import APIView, View
from rest_framework.response import Response
from django.shortcuts import render
from .models import Ingrediente
from .serializers import IngredienteSerializer
from rest_framework import status
from .forms import IngredienteForm
from silk.profiling.profiler import silk_profile

# Create your views here.
class IngredienteView(APIView):
    permission_classes = []
    @silk_profile(name="Ingrediente get")
    def get(self, request):
        id = request.data['Ingrediente']
        queryset = Ingrediente.objects.get(id=id)
        serializer = IngredienteSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    @silk_profile(name="Ingrediente Post")
    def post(self, request):
        nombre = request.data['Nombre']
        descripcion = request.data['Descripcion']        
        queryset = Ingrediente(Nombre=nombre, Descripcion=descripcion)
        queryset.save()
        serializer = IngredienteSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

class DeleteIngredienteView(APIView):
    permission_classes = []

    def post(self, request):
        id = request.data['Ingrediente']
        queryset = Ingrediente.objects.get(id=id)
        queryset.delete()
        return Response(status=status.HTTP_200_OK)

class IngredienteNewView(View):
    @silk_profile(name="Obtener Ingredientes")
    def get(self, request):
        form = IngredienteForm()
        queryset = Ingrediente.objects.all();
        return render(request, 'ingrediente.html', {'form': form,'object_list': queryset})

    @silk_profile(name="Ingresar Ingredientes")
    def post(self, request):
        form = IngredienteForm(request.POST or None)
        if form.is_valid():
            ingrediente = form.save(commit=False)
            ingrediente.save()
        form = IngredienteForm()
        queryset = Ingrediente.objects.all()
        return render(request, 'ingrediente.html', {'form': form,'object_list': queryset})