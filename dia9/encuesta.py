from pregunta import Pregunta

class Encuesta():
    def __init__(self, nombre:str, preguntas:list):
        self.nombre = nombre
        self.__preguntas = [
            Pregunta(
                p["enunciado"],
                p["ayuda"],
                p["alternativas"],
                p["requerido"],
            ) for p in preguntas
        ]
        # numeros = [2*x for x in range(10)] # [0,1,2,3,4,5,6,7,8,9]
        # numeros = []
        # for x in range(10):
        #     numeros.append(x)
        self.__listados_respuestas = []

    def mostrar_encuesta(self):
        print(self.nombre)

        for p in self.__preguntas:
            p.mostrar_pregunta()

    def agregar_listado_respuestas(self, listado_respuestas):
        self.__listados_respuestas.append(listado_respuestas)
        
class EncuestaLimitadaEdad(Encuesta):
    
    def __init__(self, nombre:str, preguntas:list, edad_min:int, edad_max:int):
        super().__init__(nombre, preguntas) #ejecutar el constructor del padre con los arg nombre y preguntas

        self.__edad_min = edad_min
        self.__edad_max = edad_max

    @property
    def edad_min(self):
        return self.__edad_min #obtener informacion Get

    @edad_min.setter
    def edad_min(self, nuevo_min):
        self.__edad_min = nuevo_min #modificar informacion
    
    @property
    def edad_max(self):
        return self.__edad_max

    @edad_max.setter
    def edad_max(self, nuevo_max):
        self.__edad_max = nuevo_max

    def agregar_respuesta(self, respuestas:list): #estas respuestas vienen de la clase ListadoRespuestas
        if self.__edad_min <= respuesta.usuario.edad <= self.__edad_max: #esto debe venir de la clase usuario
            super().agregar_listado_respuestas(respuestas)






