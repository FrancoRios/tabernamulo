from django import forms
from .models import Trago, Ingrediente

class TragoForm(forms.ModelForm):
    class Meta:
        model = Trago
        fields = ['nombre', 'tipo', 'grados']

        labels = {
            'nombre': 'Nombre',
            'tipo': 'Tipo',
            'grados': 'Grados de alcohol',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'grados': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
