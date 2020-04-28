from django.test import TestCase, SimpleTestCase
from Restaurante.models import Restaurante
from Restaurante.forms import RestauranteForm
# Create your tests here.

class TestModelRestaurante(TestCase):

    def Test_Restaurante_create(self):
        Restaurante(
            Nombre='nuevo restaurante',
            Direccion='Cuidad de guatemala'
        ).save()
        restaurantes = Restaurante.objects.all()
        restaurante = Restaurante.objects.get(id=1)
        self.assertEqual(restaurantes.count(),1)
        self.assertEqual(restaurante.Nombre,'nuevo restaurante')

class TestFormRestaurante(SimpleTestCase):

    def test_form_restaurante(self):
        form = RestauranteForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),2)
        
