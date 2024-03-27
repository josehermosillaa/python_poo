class Foto():
    def __init__(self, imagen:str,ancho:int, alto:int):
        self.__imagen = imagen
        self.__ancho = ancho
        self.__alto = alto
        self.__reacciones = 0

    @property
    def imagen(self):
        return self.__imagen

    @imagen.setter
    def imagen(self, imagen:str):
        self.__imagen = imagen
    """ completar los getters y setters faltantes"""

class FotoDePerfil(Foto):
    def __init__(self):
        super().__init__("extras/user.png", 400, 400)
        self.__recorte = [(0,0), (self.ancho,0), (0,self.alto),(self.ancho, self.alto)]


class Usuario():
    def __init__(self, correo:str, contrasena:str):
        self.__correo = correo
        self.__contrasena = contrasena
        self.__album_fotos = []
        self.__foto_perfil = FotoDePerfil()

    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self, correo):
        self.__correo = correo

    """Tarea realizar los getter y setter faltantes"""

    @property
    def album_fotos(self):
        return self.__album_fotos

    def agregar_fotos(self, imagen:str, ancho:int, alto:int):
        self.__album_fotos.append(Foto(imagen, ancho, alto))
    
    @property
    def foto_perfil(self):
        return self.__foto_perfil
    
    def actualizar_foto(self, imagen:str, ancho:int, alto:int):
        self.__foto_perfil.imagen = imagen
        self.__foto_perfil.ancho = ancho
        self.__foto_perfil.alto = alto

    def reaccionar(self, foto):
        foto.reacciones += 1
        #setter