from jugador import Jugador
from monstruo import Monstruo


m = Monstruo(hp=950, atk=1, df=8, nombre="Begimo")
m.mostrar_dialogo("GRAAAWR")
enfrentados = [Jugador(500,10,5, "espada"),m]
atk = 0


count = 0
while any(e.hp <=0 for e in enfrentados) == False:
    count +=1
    print(count)
    for e in enfrentados:
        if atk:
            e.defensa(atk)
        if e.hp > 0:
            atk = e.ataque()
        else:
            if isinstance(e, Monstruo):
                print("Felicidades!, Haz ganado la batalla!")
            elif  isinstance(e, Jugador):
                print(f" Oh no !, haz perdido la batalla :(")