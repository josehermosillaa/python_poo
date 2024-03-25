from sin_gluten import SinGluten
from abc import ABC, abstractmethod

class Chocolate(ABC):
    def __init__(self, porc_cacao:float):
        self.porc_cacao = self.validar_porc_cacao(porc_cacao)

    def validar_porc_cacao(self, porc:float) ->float:
        pass

class ChocolateAmargo(Chocolate):
    def validar_porc_cacao(self, porc:float):
        return min(max(0.75,porc), 0.85)

class ChocolateAmargoSinGluten(ChocolateAmargo,SinGluten):
    pass

c = ChocolateAmargo(0.8) #paso un porcentaje y me da el que deberia ser si fuera amargo

print(c.porc_cacao)

sg = ChocolateAmargoSinGluten(0.76)
print(sg.tipo_producto)
print(sg.porc_cacao(0.76))