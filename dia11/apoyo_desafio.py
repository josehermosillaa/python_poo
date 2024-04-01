from error import DimensionError

class Foto():
    #maximo de la foto (ancho y alto) px
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho > Foto.MAX:
            raise DimensionError("Ancho no permitido.", ancho, Foto.MAX)
        elif ancho < 1:
            raise DimensionError("Ancho debe ser mayor a 0.", ancho)
        else:
            self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto > Foto.MAX:
            raise DimensionError("Alto no permitido.", ancho, Foto.MAX)
        elif alto < 1:
            raise DimensionError("Alto debe ser mayor a 0.", ancho)
        else:
            self.__alto = alto