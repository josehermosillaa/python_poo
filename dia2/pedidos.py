from te import Te

sabor = int(input(f"""Que sabor de te desea? (Ingrese numero de la opcion)
1. Te negro
2. Te verde
3. Te de hierbas
"""))

formato = int(input(f""" Que formato desea?. 
Tenemos disponible 300 y 500 gramos. Ingrese el formato: """))

tiempo, recomendacion = Te.retornar_tiempo_y_recomendacion(sabor)
precio = Te.retorna_precio(formato)

if sabor == 1:
    sabor_texto = "Te negro"
elif sabor == 2:
    sabor_texto = "Te verde"
elif sabor  == 3:
    sabor_texto = "Agua de Hierbas"

print(f"""se ingreso su pedido de {sabor_texto}, en formato {formato} gramos,
el cual tiene un valor de ${precio}. Este te tiene un tiempo de preparacion de {tiempo} minutos,
y se recomienda su uso {recomendacion}
""")