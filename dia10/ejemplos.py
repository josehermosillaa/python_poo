consultar = True

while consultar:
    try:
        edad = int(input("Ingrese su edad : \n"))
        consultar = False
        print(edad)
        print(0/edad)

    except ValueError:
        print("debe ingresar un numero")
    except ZeroDivisionError:
        print("se esta dividiendo por cero")
    # except KeyboardInterrupt:
    #     print("se intento terminar la ejecucion del codigo")
# edad = int(input("Ingrese su edad : \n"))
# consultar = False
# print(edad)