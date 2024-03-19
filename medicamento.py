class Medicamento():
    descuento = 0.05 # 5/100
    IVA = 0.19 #19/100

    @staticmethod
    #sabemos que es una funcion pero que tiene relacion con la clase
    def validar_mayor_a_cero(numero:int):
        return numero > 0 #True o False