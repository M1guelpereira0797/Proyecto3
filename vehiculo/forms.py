from django import forms
from vehiculo.models import Vehiculo
class Buscar_carro(forms.Form):
  nombre = forms.CharField(max_length=100)

class CarrosForm(forms.ModelForm):
  class Meta:
    model = Vehiculo
    fields = ['marca_del_carro', 'modelos_del_carro', "color_del_carro"]