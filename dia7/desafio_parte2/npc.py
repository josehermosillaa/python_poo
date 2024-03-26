class NPC():
    def __init__(self, nombre:str, **kwargs):
        super().__init__(**kwargs) #que se pueden considerar como diccionario y no tiene limites de argumentos
        self.__nombre = nombre
    
    def mostrar_dialogo(self, mensaje:str):
        print(f"{self.__nombre} : {mensaje}")