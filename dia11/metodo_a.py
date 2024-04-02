from datetime import datetime


try:
    edad = int(input("Ingrese su edad: \n"))
except Exception as e:
    with open(f"error.log","a+") as log:
        log.seek(0)
        print(log.read())
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Error: {e}\n")
        log.seek(0)
        print(log.read())

        #en el with se realiza la operacion de apertura y cierre del archivo
