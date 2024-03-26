class PelotaDeDeporte():
    def __init__(self, color:str):
        self.__color = color
        # self.__tamanio = tamanio
        

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,color):
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
    def hacer_saque(self, altura:int, fuerza:int) -> tuple:
        return (altura, altura*fuerza)

class PelotaDeFutbol(PelotaDeDeporte):
    def __init__(self, color:str, cantidad_hexagonos:int):
        super().__init__(color) #se ejecuta el constructor del padre

        self.__cantidad_hexagonos = cantidad_hexagonos

    @property
    def cantidad_hexagonos(self):
        return self.__cantidad_hexagonos
    
    def hacer_pase(self, destino:str,fuerza:int) -> tuple:
        return (destino, fuerza*0.5)

pdf = PelotaDeFutbol('Blanco y negro', 15)
print(pdf.color)
print(pdf.cantidad_hexagonos)

pdt = PelotaDeTenis()
pdt.color = "Rojo"


print(pdt.color)


pelotas = [pdf, pdf, pdt, pdt,pdf]

for p in pelotas:
    if isinstance(p, PelotaDeTenis) == False:
        p.color = "Roja"
    if isinstance(p, PelotaDeFutbol):
        print(p.hacer_pase("jugador 2",  3))
    elif isinstance(p, PelotaDeTenis):
        print(p.hacer_saque(2,3))
