import random
from personaje import Personaje

class Jugador(Personaje):
    def __init__(self, hp:int, atk:int, df:int, arma:str = None):
        super().__init__(hp, atk, df)
        self.arma = arma
        
    def ataque(self):
        extra = random.randint(1,5) if self.arma else 0 
        return (self.atk + extra)

    def defensa(self, ataque:int):
        self.hp -= max(ataque - random.randint(1, self.df),0)
