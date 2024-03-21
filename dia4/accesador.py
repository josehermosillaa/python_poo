from random import choices
class Pelota():
#c           p = Pelota('Amarillo', 16, 'plastico')
    def __init__(self, color:str, tamanio = 20, material = 'plastico'):
        self.color = color #'Amarillo'
        self.tamanio = tamanio #16
        self.material = material #'plastico'

    #metodo accesador (getter)

    @property
    def color_y_material(self):
        return f"Pelota: {self.color} de {self.material}"
        # lista = ['rojo', 'azul','verde']
        # return  choices(lista)[0]
    #getter
    @property
    def tamanio(self):
        return self.tamanio
    #mutador o setter
    @tamanio.setter
    def tamanio(self, tamanio:int):
        self.tamanio = tamanio if tamanio > 0 else 1








p = Pelota('Amarillo', 16)
print(p.color_y_material)

p.tamanio = 0
print(p.tamanio)

# print(p.color, p.material, p.tamanio)
p1 = Pelota(tamanio=10, color='rojo', material='Gomoa')
print(p1.color_y_material)
# print(p1.color, p1.material, p1.tamanio)
#p1.color = 'verde'
#la ventaja de generarlo a traves de un metodo es que podemos validar la entrada