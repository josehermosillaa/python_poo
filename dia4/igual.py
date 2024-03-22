class Pelota():
    def __init__(self,color, tamanio=1):
        self.color = color
        self.tamanio = tamanio

    def __eq__(self, other):
        return self.tamanio == other.tamanio #and self.color == other.color
    
p1 = Pelota('Amarillo')
p2 = Pelota('gris')

#primera prueba
print(p1)
print(p2)
print(p1 == p2)