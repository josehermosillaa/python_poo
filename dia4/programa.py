from medicamentos3 import Medicamento

nombre = input("Ingrese el nombre del medicamneto: ")
stock = int(input("Ingrese stock del medicamento: "))
precio_bruto = int(input("Ingrese el precio del producto"))

m1 = Medicamento(nombre, stock)
m1.precio_bruto = precio_bruto
print(f"El precio bruto del medicamento {m1.nombre} es {m1.precio_bruto}")