
import time

try:
    edad = int(input("Ingrese su edad: \n"))
except Exception as e:
    with open(f"{round(time.time())}.log","r+") as log:
        log.write(f"Error: {e}") 
        #en el with se realiza la operacion de apertura y cierre del archivo
