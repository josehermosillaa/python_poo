import json

class Producto():
    def __init__(self, nombre:str, precio:int):
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
        return f"Nombre:{self.nombre} , Precio: {self.precio}"



instancias = [] 
with open("productos.txt") as productos:
    linea = productos.readline()
    while linea:
        producto = json.loads(linea) # dict
        # print(type(producto))
        instancias.append(Producto(producto.get("nombre"), producto.get("precio")))
        
        # instancias.append(Producto(producto["nombre"], producto["precio"]))

        linea = productos.readline() #next


for i in instancias:
    print(i)
# import json

# archivo = open("a.json","r+")
# datos = json.load(archivo)
# archivo.close()
# print(datos)