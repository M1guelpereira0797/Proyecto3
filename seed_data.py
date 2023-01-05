from vehiculo.models import Vehiculo
Vehiculo(marca_del_carro="Ford", modelos_del_carro="Explorer", color_del_carro="Vinotinto", ano_del_carro=2015).save()
Vehiculo(marca_del_carro="Toyota", modelos_del_carro="Tacoma", color_del_carro="Negro", ano_del_carro=2023).save()
Vehiculo(marca_del_carro="Chevrolet", modelos_del_carro="Onix RS", color_del_carro="Blanco", ano_del_carro=2023).save()
Vehiculo(marca_del_carro="Renault", modelos_del_carro="Megane", color_del_carro="Rojo", ano_del_carro=2020).save()
print("Se cargo con éxito los nuevos vehiculos en la base de datos")