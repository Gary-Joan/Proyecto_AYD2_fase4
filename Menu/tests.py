from django.test import TestCase
from Menu.models import Menu, Menu_Ingrediente
from Ingrediente.models import Ingrediente

# Create your tests here.

'''
class TestModelMenu(TestCase):

    def test_model_menu(self):
        Ingrediente.objects.create(
            Nombre='ingrediente de menu',
            Descripcion='ingrediente de prueba para el menu'
        )

        ingrediente = Ingrediente.objects.get(id=1)

        menu = Menu(
            Nombre='nombre de menu',
            Descripcion='prueba de un menu',
            Precio='Q50'
        )
        menu.save()

        #ingrediente = menu.Ingredientes.create(
        #    Nombre='ingrediente de menu',
        #    Descripcion='ingrediente de prueba para el menu'
        #)
        ingrediente.save()

        #menu.add(ingrediente)

        menus = Menu.object.all()
        #menu = Menu.objects.get(id=1)
        self.assertEquals(menus.count(), 1)
        self.assertEquals(menu.Nombre, 'nombre de menu')

    def test_model_menu_ingrediente(self):
        Ingrediente(
            Nombre='ingrediente de menu',
            Descripcion='ingrediente de prueba para el menu'
        ).save()

        ingrediente = Ingrediente.objects.get(id=1)

        Menu(
            Nombre='nombre de menu',
            Descripcion='prueba de un menu',
            Ingredientes=ingrediente,
            Precio='Q50'
        ).save()

        menu = Menu.objects.get(id=1)

        Menu_Ingrediente(
            Menu=menu,
            Ingrediente=ingrediente,
            Disponible='true',
            Cantidad=5,
            Dimensional=40
        ).save()

        menus_ingredientes = Menu_Ingrediente.object.all()
        menu_ingrediente = Menu_Ingrediente.get(id=1)
        self.assertEquals(menus_ingredientes.count(), 1)
        self.assertEquals(menu_ingrediente.Cantidad, 5)
'''