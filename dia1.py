#Los nombres de Clase se escriben con la primera letra en mayuscula
#si necesita generar un espacio en el nombre de la clase se suele usar camelCase

#ej si quiero colocar una clase que tenga de nombre Dia de cumpleaños
#el nombre seria -> class DiaDeCumpleaños

class Pelota():
    forma = "redondeada"
    material = "plastico"

pelota = Pelota() #instancia de la clase

print(type(pelota))
print(pelota.forma)
print(pelota.material)


# class Medicamento():
#     descuento = 0.05 # 5/100
#     IVA = 0.19 #19/100

#     def calcular_iva():
#         pass
#podriamos por ejempplo agregar parametros de entrada a la clase
#para que al crear una instancia se deba ingresar el precio sin IVA
#entonce se puede generar metodos para: 
# -> calcular el IVA
# -> calcular el precio con IVA -descuento 
# a traves de los metodos
