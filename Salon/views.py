from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Salon
from .serializers import SalonSerializer
from rest_framework import status
from .forms import SalonForm

# Create your views here.
class SalonView(APIView):
    permission_classes = []

    def get(self, request):
        id = request.data['Salon']
        salon = Salon.objects.get(id=id)
        serializer = SalonSerializer(salon, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        nombre = request.data['Nombre']
        descripcion = request.data['Descripcion']
        capacidad = request.data['Capacidad']
        salon = Salon(Nombre = nombre, Descripcion = descripcion, Capacidad = capacidad)
        salon.save()
        serializer = SalonSerializer(salon, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

class DeleteSalonView(APIView):
    permission_classes = []

    def post(self, request):
        id = request.data['Salon']
        salon = Salon.objects.get(id=id)
        salon.delete()
        return Response(status=status.HTTP_200_OK)

def SalonNewView(request):
    if request.method == "POST":
        form = SalonForm(request.POST)
        if form.is_valid():
            salon = form.save(commit=False)
            salon.save()
    form = SalonForm()
    return render(request, 'salon_new.html', {'form': form})

def SalonSimpleView(request):
    queryset = Salon.objects.filter()[:5]
    return render(request, 'salon.html', {'object_list':queryset})