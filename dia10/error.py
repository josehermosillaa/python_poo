class Error(Exception):
    pass

class HoraError(Error):
    pass

class LargoTexto(Error):
    def __init__(self, mensaje:str, texto:str, largo:int):
        self.mensaje = mensaje
        self.texto = texto if texto is len(texto) > 150 else None
        self.largo = largo

    def __str__(self):
        if self.texto is None and self.largo is None :
            return super().__str__()
        else:
            ret =f"{self.mensaje}"

            if self.texto != None:
                ret += f"texto ingresado: {self.texto}"
            if self.largo !=None:
                ret += f"Maximoy {self.largo} caracteres permitido"
            
            return ret
                