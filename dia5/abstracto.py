from abc import ABC, abstractmethod


class Pelota(ABC):
    @abstractmethod
    def rebotar(self, altura: int):
        pass


class PelotaDeJuguete(Pelota):
    def __init__(self, color):
        self.rebotes = []
        self.__color = color

    def rebotar(self, altura: float):
        self.rebotes = []
        while altura > 0:
            self.rebotes.append(altura)
            self.rebotes.append(0)
            altura = altura // 2
        return self.rebotes

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, nuevo_color):
        self.__color = nuevo_color


p = PelotaDeJuguete("Amarilla")

print(p.color)
p.color = "Rojo"
print(p.color)

# p.rebotar()
