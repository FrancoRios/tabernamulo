from django.test import TestCase
from apps.Registro.models import Trago
from apps.Registro.forms import TragoForm

class TragoFormCase(TestCase):
    """Prueba con datos correctos"""
    def test_valid_form(self):
        trago = Trago.objects.create(nombre='Chimbombo',tipo='fermentado', grados=20)
        data = {'nombre': trago.nombre, 'tipo': trago.tipo,'grados': trago.grados, }
        form = TragoForm(data=data)
        self.assertTrue(form.is_valid())
    """Prueba con campo 'nombre' en blanco"""
    def test_invalid_form(self):
        trago = Trago.objects.create(nombre='',tipo='fermentado', grados=20)
        data = {'nombre': trago.nombre, 'tipo': trago.tipo,'grados': trago.grados, }
        form = TragoForm(data=data)
        self.assertTrue(form.is_valid())
    """Prueba con campo 'tipo' en blanco"""
    def test_invalid_form2(self):
        trago = Trago.objects.create(nombre='Primavera',tipo='', grados=10)
        data = {'nombre': trago.nombre, 'tipo': trago.tipo,'grados': trago.grados, }
        form = TragoForm(data=data)
        self.assertTrue(form.is_valid())
    """Prueba con campo 'grados' con número negativo"""
    def test_invalid_form3(self):
        trago = Trago.objects.create(nombre='Sol y Lluvia',tipo='fermentado', grados=-10)
        data = {'nombre': trago.nombre, 'tipo': trago.tipo,'mensualidad': trago.grados, }
        form = TragoForm(data=data)
        self.assertTrue(form.is_valid())
