from django.test import TestCase, SimpleTestCase
from Montaje.models import Montaje
from Montaje.forms  import MontajeForm
# Create your tests here.
class TestModelMontaje(TestCase):

    def test_montaje_create(self):
        Montaje(
            Titulo='montaje de titulo',
            Descripcion='descripcion de test'
        ).save()
        montajes = Montaje.objects.all()
        montaje = Montaje.objects.get(id=1)
        self.assertEquals(montajes.count(),1)
        self.assertEquals(montaje.Titulo,'montaje de titulo')

class TestFormMontaje(SimpleTestCase):

    def test_montaje_form(self):
        form = MontajeForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)

    def test_montaje_form_data(self):
        form = MontajeForm(data={
            'Titulo':'prueba formulario',
            'Descripcion':'Prueba de montaje'
        })
        self.assertTrue(form.is_valid())