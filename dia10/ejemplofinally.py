from exepcion import EdadError

intentos = 0
while intentos <=3:
    try:
        edad = int(input("Ingrese su edad:\n"))
        #esto es ejercicio 3
        if edad < 0:
            raise EdadError("Edad debe ser un numero positivo", edad)
        divisor = int(input("Ingrese número para dividir su edad:\n"))
        print(edad / divisor)
        consultar = False
    except ValueError:
        print("Debe ingresar un número")
    except ZeroDivisionError:
        print("El N° por el cual desea dividir no puede ser cero")
    except Exception as e:
        print(f"ERROR: {e}")
    except:
        print("ERROR SIN INFORMACIÓN")
    finally:
        intentos += 1
        print("El numero de intentos es :", intentos)

    