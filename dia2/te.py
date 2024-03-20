class Te():
    duracion = 365
    
    # def __init__(self):
    #     self.tipo = "negro"

    # valores:
    #  1: Corresponde a Té negro
    #  2: Corresponde a Té verde
    #  3: Corresponde a Agua de hierbas.

    # Ejemplo
    def metodo_no_estatico(self):
        print("Hola soy un metodo no estatico")

    @staticmethod
    def retornar_tiempo_y_recomendacion(sabor:int):
        if sabor == 1:
            return 3, "Al desayunar"
        elif sabor == 2:
            return 5, "Al mediodía"
        elif sabor == 3:
            return 6, "Al anochecer"
    #formatos pemitidos son 300 g y 500 g
    @staticmethod
    def retorna_precio(formato):
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000
    
Te.metodo_no_estatico()
# tecito = Te()
# tecito.metodo_no_estatico()