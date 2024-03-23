class Producto():
    def __init__(self, nombre:str, precio:int, stock:int):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock if stock > 0 else 0 #validando que el stock siempre sea mayor o igual a 0

        @property
        def nombre(self):
            return self.__nombre

        """debe crear el metodo getter para precio """
        @property
        def stock(self):
            return self.__stock
        @stock.setter
        def stock(self, nuevo_stock): #yo no sumo o resto el stock, lo que me lla es un numero
            self.__stock = nuevo_stock if nuevo_stock > 0 else 0 #con esto actualizo el stock 

        def __add__(self,other):
            return  self.stock + other.stock
        def __sub__(self, other):
            return  self.stock - other.stock
        def __eq__(self,other):
            return self.nombre == other.nombre



    