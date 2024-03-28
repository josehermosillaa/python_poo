class Error(Exception):
    pass

class EdadError(Error):
    def __init__(self, mensaje, edad):
        self.mensaje = mensaje
        self.edad = edad
        