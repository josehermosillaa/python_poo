"""Herencia Simple
"""
# class PelotaDeDeporte(): #padre 
#     def __init__(self, color:str):
#         self.__color = color

#     @property
#     def color(self)-> str:
#         return self.__color 

# class PelotaDeFutbol(PelotaDeDeporte):
    
#     def mostrar_color(self): #hijo Herencia simple
#         print(f"Mi color es {self.color}")

# pdf = PelotaDeFutbol("Blanco y Negro")
# pdf.mostrar_color()

"""Herencia multiples"""

class PelotaDeDeporte():
    tipo = "Deporte"

class PelotaDePlastico():
    tipo = "Plastico"

class PelotaDePingPong(PelotaDeDeporte,PelotaDePlastico):
    pass

print(PelotaDePingPong.tipo)