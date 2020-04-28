from django.test import TestCase
from User.models import User

# Create your tests here.
class UserTest(TestCase):

    def test_create_user(self):
        User(
            cui=123456789101,
            nombre_completo="Prueba usuario",
            numero_telefono="12345678"
        ).save()
        usuarios = User.objects.all()
        usuario1 = User.objects.get(id=1)
        self.assertEquals(usuarios.count(),1)
        self.assertEquals(usuario1.nombre_completo,"Prueba usuario")
