from alternativa import Alternativa
class Pregunta():
    def __init__(self, enunciado:str, ayuda:str, alternativas:list, requerido:bool):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.__alternativas = [Alternativa(a["contenido"], a["ayuda"]) for a in alternativas ] #por cada lista de alternativas podriamos agregar ayuda y contenio
        #[a,b,c]
        self.requerido = requerido

    def mostrar_pregunta(self):
        print(self.enunciado)

        if self.ayuda:
            print(self.ayuda)
        
        for a in self.__alternativas:
            a.mostrar_alternativa()
