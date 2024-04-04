class Anuncio():
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
        

class Video(Anuncio):
    FORMATO = "Video"
    SUBTIPOS = ("instream", "outstream")

    def __init__(self,ancho:int, alto:int,url_archivo:str, url_clic:str, sub_tipo:str, duracion:int):
        super().__init__(1, 1,url_archivo,url_clic, sub_tipo) #ejecutame el constructor del padre para definir todos estos parametros
        self.__duracion = duracion if duracion >0 else 5

class Display(Anuncio):
    FORMATO = "Display"
    SUBTIPOS = ("tradicional", "native")
    
    def __init__(self,ancho:int, alto:int,url_archivo:str, url_clic:str, sub_tipo:str):
        super().__init__(ancho, alto, url_archivo,url_clic, sub_tipo) #ejecutame el constructor del padre para definir todos estos parametros


class Social(Anuncio):
    FORMATO = "Social"
    SUBTIPOS = ("facebook", "linkedin")

    def __init__(self,ancho:int, alto:int,url_archivo:str, url_clic:str, sub_tipo:str):
        super().__init__(ancho, alto, url_archivo,url_clic, sub_tipo) #ejecutame el constructor del padre para definir todos estos parametros