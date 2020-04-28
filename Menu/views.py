from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Menu, Menu_Ingrediente
from .serializers import MenuSerializer
from rest_framework import status

from .forms import MenuForm, MenuIngredienteForm
from silk.profiling.profiler import silk_profile
# Create your views here.
class MenuView(APIView):
    permission_classes = []
    @silk_profile(name='Menu')
    def get(self, request):
        id = request.data['Menu']
        queryset = Menu.objects.get(id=id)
        serializer = MenuSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    @silk_profile(name='Menu2')
    def post(self, request):
        nombre = request.data['Nombre']
        descripcion = request.data['Descripcion']
        precio = request.data['Precio']        
        queryset = Menu(Nombre=nombre, Descripcion=descripcion, Precio=precio)
        queryset.save()
        serializer = MenuSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

class DeleteMenuView(APIView):
    permission_classes = []

    def post(self, request):
        id = request.data['Menu']
        queryset = Menu.objects.get(id=id)
        queryset.delete()
        return Response(status=status.HTTP_200_OK)

@silk_profile(name='vista Menu')
def MenuNewView(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
    form = MenuForm()
    return render(request, 'menu_new.html', {'form': form})
    
def MenuSimpleView(request):
    queryset = Menu.objects.filter()[:5]
    return render(request, 'menu.html', {'object_list':queryset})

@silk_profile(name='vista ingredientes')
def MenuIngredienteNewView(request):
    if request.method == "POST":
        form = MenuIngredienteForm(request.POST)
        if form.is_valid():
            menu_ingrediente = form.save(commit=False)
            menu_ingrediente.save()
    form = MenuIngredienteForm()
    queryset = Menu_Ingrediente.objects.filter()
    return render(request, 'menu_ingrediente_new.html', {'form': form,'object_list':queryset})

def MenuIngredienteSimpleView(request):
    queryset = Menu_Ingrediente.objects.filter()[:5]
    return render(request, 'menu_ingrediente.html', {'form': form,'object_list':queryset})