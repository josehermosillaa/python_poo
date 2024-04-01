class Error(Exception):
    """Clase Base Excepciones"""
    pass

class DimensionError(Error):
    def __init__(self, mensaje:str, dimension:int, maximo:int):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            ret = self.mensaje
            if self.dimension:
                ret += f" se ingreso dimensión {self.dimension}."
            if self.maximo:
                ret += f" EL valor de máximo permitido es {self.maximo}"
            return ret


# ret = "Hola Mundo"
# mensaje = "como estas"

# ret = ret + mensaje
# ret += mensaje
# #output =  "Hola Mundocomo estas"