import random
from personaje import Personaje

class Jugador(Personaje):
    
    def ataque(self):
        extra = random.randint(1,5) if self.arma else 0 
        return (self.atk + extra)

    def defensa(self, ataque:int):
        self.hp -= max(ataque - random.randint(1, self.df),0)
