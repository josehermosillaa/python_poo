consultar = True
while consultar:
    try:
        edad = int(input("Ingrese su edad:\n"))
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