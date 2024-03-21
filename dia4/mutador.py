from random import choices
class Pelota():
#c           p = Pelota('Amarillo', 16, 'plastico')
    def __init__(self,  tamanio = 20, material = 'plastico'):
        self.__tamanio_pelota = tamanio #16
        self.material = material #'plastico'
        
    #getter
    @property
    def tamanio(self):
        return self.__tamanio_pelota
    #mutador o setter
    @tamanio.setter
    def tamanio(self, tamanio_pelota:int):
        self.__tamanio_pelota = tamanio_pelota if tamanio_pelota > 0 else 1



p = Pelota()
print(p.tamanio) #accesador
# print(p.__tamanio_pelota)

#intentamos cambiar su valor a cero
p.tamanio = 0
print(p.tamanio) #accesador

"""El doble guion bajo sirve para que los atributos sean solo accedidos a traves
de los metodos getter y setter (sean "privados" )

"""

