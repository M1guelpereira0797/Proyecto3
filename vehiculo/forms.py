from django import forms
class Buscar_carro(forms.Form):
    nombre = forms.CharField(max_length=100)