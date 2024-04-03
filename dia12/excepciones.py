import json
from datetime import datetime
#objeto de fecha y hora
class Producto():
    def __init__(self, nombre:str, precio:int):
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
        return f"Nombre:{self.nombre} , Precio: {self.precio}"



""" EJEMPLO PARA DESARROLLAR LA SEGUNDA PARTE DEL DESAFIO"""
instancias = [] 
with open("productos.txt") as productos:
    linea = productos.readline() #se ubica en la primera linea del txt
    while linea:
        try:
            producto = json.loads(linea) # dict
            # print(type(producto))
            instancias.append(Producto(producto.get("nombre"), producto.get("precio")))
        # instancias.append(Producto(producto["nombre"], producto["precio"]))
        except Exception as e:
            with open("error.log", "a+") as log:
                now = datetime.now()
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Error: {e}\n")
        finally:
            linea = productos.readline() #next

for i in instancias:
    print(i)