class OrdenCompra():
    #Se crea un metodo de instancia para definir atributos
    
    # def __init__(self):
    #     #atributos de instancia
    #     self.identificador = 0
    #     self.total_productos = 0 
    #     self.monto = 0
    #     self.codigo_descuento = ""
    
    def nueva_orden(self):
        #atributos de instancia
        self.identificador = 0
        self.total_productos = 0 
        self.monto = 0
        self.codigo_descuento = ""

    def asigna_monto(self, dinero):
        self.monto = dinero
        if self.monto > 20000:
            self.codigo_descuento = "20PORCIENTO"
        elif self.monto > 10000:
            self.codigo_descuento = "10PORCIENTO"