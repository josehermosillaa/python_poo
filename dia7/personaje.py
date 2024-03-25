from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, hp:int, atk:int, df:int, arma:str='')->None:
        self.hp = hp
        self.atk = atk
        self.df = df
        self.arma = arma

    @abstractmethod
    def ataque(self) ->int:
        pass
    @abstractmethod
    def defensa(self):
        pass
        