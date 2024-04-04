class Campania():
    def __init__(self, nombre:str, fecha_inicio:date, fecha_termino:date, anuncios:list):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = anuncios #aqui tendre instancias de la clase anuncios y sus hijas Display, sopcial, video


    def __str__(self):
        cant_video = 0
        cant_display = 0
        cant_social = 0
        #anuncios nos tra objetos de tipo [Video, Social, Video, Display]
        for elemento in self.__anuncios:
            if isinstance(elemento, Video):
                cant_video +=1
            elif isinstance(elemento, Display):
                cant_display+=1
            elif isinstance(elemento, Social):
                cant_social += 1
        # cant_video = len([elemento for elemento in self.anuncios if isinstance(elemento,Video)])    
        return f"""
        Nombre de la Campaña: {self.__nombre}
        Anuncios: {cant_video} Video, {cant_display} Display, {cant_social} Social
        """
