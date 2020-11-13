from django.test import TestCase
from apps.Registro.models import Trago

class TragoTestCase(TestCase):
    """Pre - escenario"""
    def setUp(self):
        Trago.objects.create(nombre="Terremoto",tipo="Típico", grados=40)
        Trago.objects.create(nombre="Pihuelo",tipo="Fuerte", grados=60)

    def test_ingresar_tragos(self):
        """Los tragos se registran correctamente en la BD"""
        trago_1 = Trago.objects.get(nombre="Terremoto")
        trago_2 = Trago.objects.get(nombre="Pihuelo")
        self.assertEqual(trago_1.grados, 40)
        self.assertEqual(trago_2.grados, 60)
