class Pelota():

    """ al ejecutar la funcion asigna_color, se creara el atributo color
    por la referencia a la propia instancia creada"""
    #color = "Rojo"
    #self.color = nuevo_color

    def inicio_pelota(self):
        self.material = ""
        self.color = ""
        self.tamano = 20

    #metodo de instancia que asigna valor
    def asigna_color(self, nuevo_color:str):
        self.color = nuevo_color

    #Metodo de instancia que lee el color de la instancia
    def leer_color(self):
        print(f"el color de esta pelota es {self.color}")
    
    #Variable de alcance del metodo (existe solo en el metodo)
    def lee_color_y_atributo(self, color_local:str):
        color = color_local

        #un metodo puede llamar a otros metodos
        self.leer_color
        print(f"el color {color_local} no es el color de ESTA pelota")





#esto es del segundo ejemplo

pelota_de_andy = Pelota()

pelota_de_andy.inicio_pelota()  #este es el estado inicial
#tamaño 20, material "" , color ""

print(pelota_de_andy.material)
print(pelota_de_andy.tamano)

pelota_de_andy.asigna_color("Azul, Amarillo") #cambio su estado
#tamaño 20, material "" , color "Azul Amarillo"
pelota_de_andy.tamano = 100
pelota_de_andy.material = "Plastico"





#esto es del primer ejemplo


# tenis = Pelota()
# futbol = Pelota()
# medicinal = Pelota()
# ping_pong = Pelota()
# basquetbol = Pelota()

# tenis.asigna_color("Amarillo")
# futbol.asigna_color("Roja")
# medicinal.asigna_color("Verde")
# ping_pong.asigna_color("blanco")
# basquetbol.asigna_color("Naranja")

# tenis.leer_color()
# futbol.leer_color()
# medicinal.leer_color()
# print()
# tenis.lee_color_y_atributo("negro")
# futbol.lee_color_y_atributo("ROSADO")
# medicinal.lee_color_y_atributo("Mostaza")