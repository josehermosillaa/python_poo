class Error(Exception):
    pass

class DimensionError(Error):
    def __init__(self, mensaje:str, dimension:int = None, maximo:int = None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        pass


