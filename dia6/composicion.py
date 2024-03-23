from abc import ABC, abstractmethod

class Material(ABC):
    @abstractmethod
    def romper(self):
        pass

class MaterialPlastico(Material):
    nombre = 'Plastico'
    duracion = 'Corta'

    def __init__(self, textura:str):
        self.textura = textura

    def romper(self):
        pass

class Pelota():
    def __init__(self, tamanio:int, color:str, textura:str):
        self.tamanio = tamanio
        self.color = color
        self.textura = textura

        self.material = MaterialPlastico(self.textura)

p = Pelota(16, 'rojo', 'rugosa')

print(p.material.nombre)
