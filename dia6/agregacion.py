class Material():
    def __init__(self, nombre:str, duracion:str, textura:str):
        #funcion que validara estos datos antes de ASIGNARLOS
        son_validos = self.validar([nombre, duracion,textura])
        if son_validos:
            self.nombre = nombre
            self.duracion = duracion
            self.textura = textura
        else:
            print("Argumento no valido")
            
    def validar(*args):
        for a in args:
            if type(a) is str:
                continue
            else:
                return False
        return True
class Pelota():
    def __init__(self, tamanio:int, color:str, material:Material):
        self.tamanio = tamanio
        self.color = color
        #material
        self.material = material 

#material
m = Material('Plastico', 'Corta', 100)

p = Pelota(16, 'Amarillo',m)

print(type(p.material))

print(p.material.nombre)
print(p.material.duracion)