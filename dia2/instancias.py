from te import Te
# Te.metodo_no_estatico()
te1 = Te()
te2 = Te()

tipo1 = type(te1)
tipo2 = type(te2)

print(tipo1)
print(tipo2)

if tipo1 == tipo2 :
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos son de distinto tipo")