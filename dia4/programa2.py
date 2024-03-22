from medicamentos3 import Medicamento

opcion_ingreso = int(input(f"""
Desea agregar otro medicamento?
1. Si
2. No
"""))

ingresados = []

while opcion_ingreso == 1:
    nombre = input("Ingrese nombre del medicamento: ")
    stock = int(input("Ingrese stock del medicamento: "))
    m = Medicamento(nombre,stock)

    if m in ingresados:
        indice = ingresados.index(m)
        ingresados[indice] += m
    else:
        ingresados.append(m)
        precio_bruto = int(input("Ingrese precio bruto: "))
        m.precio = precio_bruto

    print(f""" ********* DATOS DEL MEDICAMENTO {m.nombre} ***********
    PRECIO BRUTO: ${m.precio_bruto}""")
    if m.descuento:
        print(f"DESCUENTO: ${m.descuento * 100}%")
    print(f"PRECIO FINAL: ${m.precio_final}")
    print(f"STOCK: {m.stock}")

    print(f"La farmacia cuenta con {len(ingresados)} medicamentos")
    print(ingresados[0].stock)
    opcion_ingreso = int(input(f"""
    Desea agregar otro medicamento?
    1. Si
    2. No
"""))

