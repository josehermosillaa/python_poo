from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, hp:int, atk:int, df:int, **kwargs)->None:
        super().__init__(**kwargs)
        self.__hp = hp
        self.__atk = atk
        self.__df = df

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    @property
    def atk(self):
        return self.__atk

    @property
    def df(self):
        return self.__df    


    @abstractmethod
    def ataque(self) ->int:
        pass
    @abstractmethod
    def defensa(self):
        pass
        