class Medicamento():
    descuento = 0.05
    IVA = 0.19

    @staticmethod
    def validar_mayor_a_cero(numero:int):
        return numero > 0
    
    def asigna_precio(self, precio_entregado:int):

        es_valido = self.validar_mayor_a_cero(precio_entregado)
        if es_valido:
            self.precio = precio_entregado
        else:
            print(f"El precio {precio_entregado} no es un precio valido")