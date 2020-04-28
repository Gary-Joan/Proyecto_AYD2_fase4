from django.test import TestCase, SimpleTestCase, Client
from Salon.models import Salon
from Salon.forms import SalonForm
# Create your tests here.
class TestSalon(TestCase):
    
    def test_create_salon(self):
        Salon(
            Nombre="salon prueba",
            Descripcion="una descripcion de salon",
            Capacidad=100
        ).save()
        salones = Salon.objects.all()
        salon = Salon.objects.get(id=1)
        self.assertEquals(salones.count(),1)
        self.assertEquals(salon.Nombre,"salon prueba")

class TestFormSalon(SimpleTestCase):
    
    def test_salon_form(self):
        form = SalonForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)

    def test_salon_form_data(self):
        form = SalonForm(data={
            'Nombre':'salon form',
            'Descripcion':'prueba de form de salon',
            'Capacidad':'500'
        })
        self.assertTrue(form.is_valid())