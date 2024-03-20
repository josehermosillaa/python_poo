from medicamento2 import Medicamento

paracetamol = Medicamento()

precio = int(input("Ingrese el precio del medicamento"))

paracetamol.asigna_precio(precio)

print(paracetamol.precio)