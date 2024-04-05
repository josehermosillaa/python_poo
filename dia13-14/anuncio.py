from  abc import ABC, abstractmethod
class Anuncio(ABC):
    def __init__(self, ancho:int, alto:int, url_archivo:str, url_clic:str, sub_tipo:str):
        self.__ancho = ancho if ancho > 0 else 1 #debemos validar
        self.__alto = alto if alto > 0 else 1 #debemos validar
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__subtipo = sub_tipo
        
        """
        resultado = 1
        if ancho >0 :
            resultado = ancho
        else:
            resultado = 1
        """

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1
    
    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, alto):
        self.__alto = alto if alto > 0 else 1 

    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo

    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, url_clic):
        self.__url_clic = url_clic
    
    @property
    def sub_tipo(self):
        return self.__subtipo
    
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        self.__subtipo = sub_tipo

    @abstractmethod
    def comprimir_anuncios(self):
        pass
    @abstractmethod
    def redimensionar_anuncio(self):
            pass

class Video(Anuncio):
    FORMATO = "Video"
    SUBTIPOS = ("instream", "outstream")

    def __init__(self,ancho:int, alto:int,url_archivo:str, url_clic:str, sub_tipo:str, duracion:int):
        super().__init__(1, 1,url_archivo,url_clic, sub_tipo) #ejecutame el constructor del padre para definir todos estos parametros
        self.__duracion = duracion if duracion >0 else 5

    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self):
        pass

    def comprimir_anuncios(self):
        print("COMPRESION DE VIDEO NO IMPLEMENTADA AUN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AUN")

class Display(Anuncio):
    FORMATO = "Display"
    SUBTIPOS = ("tradicional", "native")
    
    def __init__(self,ancho:int, alto:int,url_archivo:str, url_clic:str, sub_tipo:str):
        super().__init__(ancho, alto, url_archivo,url_clic, sub_tipo) #ejecutame el constructor del padre para definir todos estos parametros

    def comprimir_anuncios(self):
        print("COMPRESION ANUNCIO DISPLAY NO IMPLEMENTADO AUN")

    def redimensionar_anuncio(self):
        print("RECORTE ANUNCIO DISPLAY NO IMPLEMENTADO AUN")


class Social(Anuncio):
    FORMATO = "Social"
    SUBTIPOS = ("facebook", "linkedin")

    def __init__(self,ancho:int, alto:int,url_archivo:str, url_clic:str, sub_tipo:str):
        super().__init__(ancho, alto, url_archivo,url_clic, sub_tipo) #ejecutame el constructor del padre para definir todos estos parametros

    def comprimir_anuncios(self):
        print("COMPRESION ANUNCIO SOCIAL NO IMPLEMENTADO AUN")

    def redimensionar_anuncio(self):
        print("RECORTE ANUNCIO SOCIAL   NO IMPLEMENTADO AUN")