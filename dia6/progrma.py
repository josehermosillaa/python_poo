from venta import Venta

venta = Venta()

opcion = int(input(f"""
Desea ingresar un item a la venta?
1. Si
2. No
    """))

while opcion == 1:
    producto = input("Ingrese nombre del producto:\n")
    cantidad = int(input("Ingrese cantidad vendida del producto: \n"))

    venta.modificar_detalle(producto, cantidad)
    opcion = int(input(f"""
Desea ingresar un item a la venta?
1. Si
2. No
    """))

print(venta.detalle)