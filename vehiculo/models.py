from django.db import models


class Vehiculo(models.Model):

    marca_del_carro = models.CharField(max_length=100)
    modelos_del_carro = models.CharField(max_length=200)
    color_del_carro = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.id}, {self.marca_del_carro}, {self.modelos_del_carro}, {self.color_del_carro}, {self.ano_del_carro}"

