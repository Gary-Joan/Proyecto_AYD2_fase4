from django.test import TestCase
from Ingrediente.models import Ingrediente
# Create your tests here.
class TestModelIngrediente(TestCase):
    
    def test_model_ingrediente(self):
        Ingrediente(
            Nombre = 'nombre de ingrediente',
            Descripcion = 'descripcion del ingrediente'
        ).save()
        ingredientes = Ingrediente.objects.all()
        ingrediente = Ingrediente.objects.get(id=1)
        self.assertEquals(ingredientes.count(),1)
        self.assertEquals(ingrediente.Nombre,'nombre de ingrediente')
        self.assertEquals(ingrediente.id,1)