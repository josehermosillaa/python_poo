
class Alternativa():
    def __init__(self, contenido: str, ayuda:str):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar_alternativa(self):
        print(self.contenido)

        if self.ayuda:
            print(self.ayuda)