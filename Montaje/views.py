from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Montaje
from .serializers import MontajeSerializer
from rest_framework import status
from .forms import MontajeForm

# Create your views here.
class MontajeView(APIView):
    permission_classes = []

    def get(self, request):
        id = request.data['Montaje']
        queryset = Montaje.objects.get(id=id)
        serializer = MontajeSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        titulo = request.data['Titulo']
        descripcion = request.data['Descripcion']
        queryset = Montaje(Titulo=titulo, Descripcion = descripcion)
        queryset.save()
        serializer = MontajeSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

class DeleteMontajeView(APIView):
    permission_classes = []

    def post(self, request):
        id = request.data['Montaje']
        queryset = Montaje.objects.get(id=id)
        queryset.delete()
        return Response(status=status.HTTP_200_OK)

def MontajeNewView(request):
    if request.method == "POST":
        form = MontajeForm(request.POST)
        if form.is_valid():
            montaje = form.save(commit=False)
            montaje.save()
    form = MontajeForm()
    return render(request, 'montaje_new.html', {'form': form})

def MontajeSimpleView(request):    
    queryset = Montaje.objects.filter()[:5]
    return render(request, 'montaje.html', {'object_list':queryset})