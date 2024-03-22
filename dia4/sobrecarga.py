
# class MiClase():
#     def __init__(self):
#         self.precio = 100
    
#     #sobrecargarlo / "sobreescribirlo"
#     def __str__(self):
#         return f"Oh no, el metodo str se ha sobrecargado {self.precio}"
# a = MiClase()
# print(a)
# b = str(a)
# c = a

# print(b)
# print(c)

#metodo add
# 1
# class Pelota():
#     def __init__(self, tamanio, color='blanco'):
#         self.tamanio = tamanio
#         self.color = color

#     def __add__(self, other):
#         return self.color + ' '+other.color

# p1 = Pelota(16)
# p2 = Pelota(32, 'Amarillo')

# print(p1 + p2)


# 2
class Coordenada():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self,other):
        nuevo_x = self.x + other.x
        nuevo_y = self.y + other.y
        return Coordenada(nuevo_x,nuevo_y)
    def __str__(self):
        return f"Coordenadas ({self.x}, {self.y}) "
        
c1 = Coordenada(5,10)
c2 = Coordenada(-5,10)
suma_coordenadas = c1 + c2

print(suma_coordenadas)
