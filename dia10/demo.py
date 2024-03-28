from error import HoraError, LargoTextoError 
from reunion import Reunion 
import re 
titulo = None 
hora = None 
#expresion regular para el formato de hora solicitado
time_re = "^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$"

while True:
    try:
        titulo = input("Ingrese el titulo de la reunion, \n(maximo 150 caracteres)")
        
        if len(titulo)>150:
            raise LargoTextoError("Titulo de la reunion excede maximo de caracteres", 150)
        if hora is None or re.search(time_re, hora) is None:
            hora = input("\nIngrese La Hora de la reunion (HH:MM:SS)")
            if re.search(time_re, hora) is None:
                raise HoraError("Formato debe ser HH:MM:SS")

    except Exception as e :
        print(f"{e}\n")
        continue
    else:
        break

r = Reunion(titulo, hora)
print("Reunion creada correctamente")