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


def IngredienteNewView(request):
    if request.method == "POST":
        form = IngredienteForm(request.POST or None)
        if form.is_valid():
            ingrediente = form.save(commit=False)
            ingrediente.save()
    form = IngredienteForm()    
    return render(request, 'ingrediente_new.html', {'form': form})    

def IngredienteSimpleView(request):
        queryset = Ingrediente.objects.filter()[:5]
        return render(request, 'ingrediente.html', {'object_list': queryset})