from django.shortcuts import render
from vehiculo.models import Vehiculo


def index(request):
    return render(request, "vehiculo/Presentacion_de_carros.html")

def buscar_carros(resquest):
    lista_de_marca_de_carros=["Mercedes", "Ferrari", "Lamborgini", "Mclaren", "Chevrolet"]
    query=resquest.GET["q"]
    if query in lista_de_marca_de_carros:
        indice_de_resultado = lista_de_marca_de_carros.index(query)
        resultado=lista_de_marca_de_carros[indice_de_resultado]
    else: 
        resultado= "no hay registro en la base de datos"
    return render(resquest, 
    "vehiculo/buscar_carros.html",
    {"resultado": resultado})

def mostrar_carros(request):
  lista_carros = Vehiculo.objects.all()
  return render(request, "vehiculo/Carros.html", {"lista_carros": lista_carros})
