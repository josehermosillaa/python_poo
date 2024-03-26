class PelotaDeDeporte():
    def __init__(self, color:str):
        self.__color = color
        # self.__tamanio = tamanio
        

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self):
        self.__color = color

class PelotaDeTenis(PelotaDeDeporte):
    def __init__(self):
        self.__color = "Amarillo"

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        pass   #esta funcion no hace nada

class PelotaDeFutbol(PelotaDeDeporte):
    def __init__(self, color:str, cantidad_hexagonos:int):
        super().__init__(color) #se ejecuta el constructor del padre

        self.__cantidad_hexagonos = cantidad_hexagonos

    @property
    def cantidad_hexagonos(self):
        return self.__cantidad_hexagonos

pdf = PelotaDeFutbol('Blanco y negro', 15)
print(pdf.color)
print(pdf.cantidad_hexagonos)




pdt = PelotaDeTenis()
pdt.color = "Rojo"

print(pdt.color)
