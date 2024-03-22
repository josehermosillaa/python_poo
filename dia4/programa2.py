from medicamentos3 import Medicamento
print("*********************BIENVENIDO AL SISTEMA DE FARMACIAS**************\n")
opcion_ingreso = int(input(f"""
Desea agregar un medicamento?
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
        ingresado = ingresados[indice]
        print(f""" ********* DATOS DEL MEDICAMENTO {ingresado.nombre} ***********
        PRECIO BRUTO: ${ingresado.precio_bruto}""")
        if m.descuento:
            print(f"DESCUENTO: ${ingresado.descuento * 100}%")
        print(f"PRECIO FINAL: ${ingresado.precio_final}")
        print(f"STOCK: {ingresado.stock}")

        print(f"La farmacia cuenta con {len(ingresados)} medicamentos")
        # print(ingresados[0].stock)
        opcion_ingreso = int(input(f"""
        Desea agregar otro medicamento?
        1. Si
        2. No
    """))
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
        # print(ingresados[0].stock)
        opcion_ingreso = int(input(f"""
        Desea agregar otro medicamento?
        1. Si
        2. No
    """))

