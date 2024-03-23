from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    @abstractmethod
    def ingresar_productos(self, nombre, precio, stock):
        pass
    
    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass

class TiendaRestaurante(Tienda):
    tipo = 'Restaurante'

    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_productos(self, nombre, precio, stock):
        p = Producto(nombre, precio, stock)

        encontrado = p in self.__productos #si lo encuentra esto es True (__eq__)
        if not encontrado: #stock es 0
            self.__productos.append(p)

    def listar_productos(self):
        if len(self.__productos)>0:
            retorno = ''
            for producto in self.__productos:
                retorno += f"""
                NOMBRE: {producto.nombre}  
                PRECIO : ${producto.precio}
                """
            return retorno
        else:
            return "No hay productos para esta tienda"
        
    def realizar_venta(self, nombre_producto, cantidad):
        pass



class TiendaFarmacia(Tienda):
    tipo = 'Farmacia'

    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []
    
    def ingresar_productos(self, nombre, precio, stock):
        p = Producto(nombre, precio, stock)

        encontrado = p in self.__productos #si lo encuentra esto es True (__eq__)
        if not encontrado: #stock es 0 (no encontrado)
            self.__productos.append(p)

        elif encontrado:
            indice = self.__productos.index(p)
            self.__productos[indice].stock = p + self.__productos[inidice] 

    def listar_productos(self):
        if len(self.__productos)>0:
            retorno = ''
            for producto in self.__productos:
                m=''
                if producto.precio > 15000:
                    m = "(Envio Gratis al solicitar este producto)"
                retorno += f"""
                NOMBRE: {producto.nombre}  
                PRECIO : ${producto.precio} 
                {m}
                """
            return retorno
        else:
            return "No hay productos para esta tienda"

    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad <=3:
            p = Producto(nombre_producto,0,cantidad) #instancia para buscar en el stopck del producto
            if  p in self.__productos:
                indice = self.__productos.index(p)
                if self.__productos[indice].stock >0:
                    print(f"el stock disponible es {self.__productos[indice].stock}") #1
                    temporal = self.__productos[indice] - p  #0 
                    nuevo_stock = temporal if temporal > 0 else 0 
                    self.__productos[indice].stock = nuevo_stock



                    #       if self.__productos[indice].stock >0:
                    # print(f"el stock disponible es {self.__productos[indice].stock}") #1
                    # if cantidad > self.__productos[indice].stock:
                    #     print("solo comprar el stock disponible")
                    #     temporal = self.__productos[indice] - p  #0 
                    #     nuevo_stock = temporal if temporal > 0 else 0 
                    #     self.__productos[indice].stock = nuevo_stoc
                    # else:
                    #     temporal = self.__productos[indice] - p  #0 
                    #     nuevo_stock = temporal if temporal > 0 else 0 
                        # self.__productos[indice].stock = nuevo_stock




