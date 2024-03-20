from mascotas import OrdenCompra

oc = OrdenCompra()

oc.nueva_orden() #inicializar los atributos de instancia en su valor por defecto

oc.identificador = int(input("Ingrese Identificador de la OC : \n"))

oc.total_productos = int(input("Ingrese el total de productos: \n"))

monto = int(input("Ingrese Monto: \n"))
oc.asigna_monto(monto)

#SE COMENTA POR LA REFACTORIZACION
# oc.monto = int(input("Ingrese Monto: \n"))

# if oc.monto > 20000:
#     oc.codigo_descuento = "20PORCIENTO"
# elif oc.monto> 10000:
#     oc.codigo_descuento = "10PORCIENTO"

print(oc.codigo_descuento)