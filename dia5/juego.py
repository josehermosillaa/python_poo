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
    numero = random.uniform(0,1)
    # resultado = ''
    resultado = 'G' if numero < probabilidad_ganar else 'P'
    # if numero< probabilidad_ganar:
    #     resultado = 'G'
    # else:
    #     resultado = 'P'
    if resultado == 'G':
        print(f"""Le has ganado al orco, Felicidades!
        Recibiras 50 puntos de experiencia!        """)
        p.estado = 50
        o.estado = -30
    elif resultado == 'P':
        print(f"""Oh No! El Orco te ha ganado!
        Has perdido 30 puntos de experiencia!       """)
        p.estado = -30
        o.estado = 50

    print(p.estado)
    print(o.estado)
    probabilidad_ganar = p.get_probabilidad_ganar(o)
    opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)

print('¡Has huido! El orco ha quedado atrás.')



