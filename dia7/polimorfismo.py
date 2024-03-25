class PelotaDePlastico():
    def __init__(self):
        self.rebotes = []
    def rebotar(self, altura):
        self.rebotes = []
        while altura>0:
            self.rebotes += [int(altura),0]
            altura //=1.1 # altura = altura //1.1

class PelotaDeJuguete(PelotaDePlastico):
    def rebotar(self, altura):
        self.rebotes = []
        while altura > 0:
            self.rebotes += [int(altura),0]
            altura //=2 # altura = altura //1.1

pdj = PelotaDeJuguete()
pdj.rebotar(5)
print(pdj.rebotes)
#llamar al metodo del padre
print(type(pdj))
super(type(pdj),pdj).rebotar(5) #se llama a las caracteristicas del
print(pdj.rebotes)