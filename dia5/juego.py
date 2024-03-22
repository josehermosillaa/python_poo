from personaje import Personaje
import random

print("Bienvenido a Gran Fantasía")

nombre = input("Por favor indique nombre de su personaje: \n")

p = Personaje(nombre)

print("Oh no, Ha aparecido un Orco!")

o = Personaje('Orco')

probabilidad_ganar = p.get_probabilidad_ganar(o)

opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)
##aca devolvemos 1 para atacar y 2 para huir y se acaba el programa

while opcion_orco == 1:
    pass
