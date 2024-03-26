class ClaseBase1:
    def __init__(self, arg1):
        self.arg1 = arg1
        print("Constructor de ClaseBase1")

class ClaseBase2:
    def __init__(self, arg2):
        self.arg2 = arg2
        print("Constructor de ClaseBase2")

class ClaseDerivada(ClaseBase1, ClaseBase2):
    def __init__(self, arg1, arg2, arg3):
        super().__init__(arg1)
        # super().__init__(arg2)
        self.arg3 = arg3
        print("Constructor de ClaseDerivada")

# Crear una instancia de ClaseDerivada
obj = ClaseDerivada("argumento1", "argumento2", "argumento3")
