
archivo = open("prueba.txt", encoding='utf-8')
# print(archivo.read())
# print(archivo.readlines())
# print(len(list(archivo.readlines())))
# print(archivo)

for linea in archivo.readlines():
    print(linea)
archivo.close()

