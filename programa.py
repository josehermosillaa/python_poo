from medicamento import Medicamento

precio = int(input("Ingrese un precio a validar"))

es_valido = Medicamento.validar_mayor_a_cero(precio) #aqui me retorna el resultado de validar_mayor_a_cero

if es_valido:
    print("el precio es valido")

else:
    print("No es valido")

m1 = Medicamento()
m2 = Medicamento()
#`segunda pregunta (tienen mismo  IVA y descuento)`
if m1.descuento == m2.descuento and m1.IVA == m2.IVA:
    print("Todas las instancias tienen igual Iva y descuento")
    print(f" el IVA es {m1.IVA*100}% y el descuento es {m1.descuento*100}%")