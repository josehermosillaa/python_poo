
class Pelota():
#c           p = Pelota('Amarillo', 16, 'plastico')
    def __init__(self, color:str, tamanio = 20, material = 'plastico'):
        self.color = color #'Amarillo'
        self.tamanio = tamanio #16
        self.material = material #'plastico'

        # print("Hola soy el constructor de pelota")

# #b           p = Pelota('Amarillo', 16, 'plastico')
#     def __init__(self, color:str, tamanio:int, material:str):
#         self.color = color #'Amarillo'
#         self.tamanio = tamanio #16
#         self.material = material #'plastico'

        # print("Hola soy el constructor de pelota")
#a
    # def __init__(self):
    #     self.color = 'blanco'
    #     self.tamanio = 20
    #     self.material = 'plastico'
    #     # print("Hola soy el constructor de pelota")
        
        



# p = Pelota('Amarillo', 16, 'plastico')
# basquetbal = Pelota('Naranja',24, 'Goma')

# print(p.color, p.material, p.tamanio)
# print(basquetbal.color, basquetbal.tamanio, basquetbal.material)

#por convencion no se suele usar la ñ
# tamaño = 30
# print(tamaño)

p = Pelota('Amarillo', 16)

print(p.color, p.material, p.tamanio)
p1 = Pelota(tamanio=10, color='rojo', material='Gomoa')
print(p1.color, p1.material, p1.tamanio)
#p1.color = 'verde'
#la ventaja de generarlo a traves de un metodo es que podemos validar la entrada