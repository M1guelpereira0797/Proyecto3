# Proyecto_final_lista_de_Carros_3
proyecto final 



{% extends 'vehiculo/base.html' %}
{% block titulo%} Lista de todos mis Familiares {% endblock %}
{% block contenido %}
    {% for Vehiculo in lista_carros %}
    <ul>
        <li> Marca: {{Vehiculo.marca_del_carro}}, Modelo:{{Vehiculo.modelos_del_carro}}, Color:{{Vehiculo.color_del_carro}}, Año:{{Vehiculo.ano_del_carro}} </li>
    </ul>
  {% endfor %}
{% endblock %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UFT-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Busca tu Carros</title>
</head>
    
<body>
   
    {{resultado}}

</body>

