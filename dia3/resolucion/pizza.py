from ingredientes import vegetales, masas, proteicos

class Pizza():

    tamano = "familiar"
    precio = 10000
    
    @staticmethod
    def validar_elemento(solicitado, posibles):
        """Todos los datos posibles deben venir en minusculas"""
        #posibles es una lista
        # for elemento in posibles:
        #     if solicitado == elemento:
        #         return True
        # return False
        return solicitado.lower() in posibles #in lo que hace es preguntar si existe el elemento en la lista
    
    def pedir(self):
        self.proteico = input(f"""Ingrese que proteina desea.
        Las posibilidades son:
        -Vacuno
        -Pollo
        -Carne Vegetal
        
        """)
        
        #es una proteina y 2 vegetales
        self.vegetales = []
        self.vegetales.append(input(f"""Ingreser el primer vegetal.
        Las opciones son:
        -Tomate
        -Aceitunas
        -Champiñones
        
        """))

        self.vegetales.append(input(f"""Ingresar el segundo vegetal.
        Las opciones son:
        -Tomate
        -Aceitunas
        -Champiñones
        
        """))

        #tipo de masa
        self.tipo_masa =input(f"""Ingresar el tipo de masa.
        Las opciones son:
        -Delgada
        -Tradicional
        
        """)

        valida_proteico = self.validar_elemento(self.proteico, proteicos)
        valida_vegetales = self.validar_elemento(self.vegetales[0],vegetales) and self.validar_elemento(self.vegetales[1],vegetales)
        valida_masa = self.validar_elemento(self.tipo_masa, masas)
        self.es_una_pizza_valida = valida_proteico and valida_vegetales and valida_masa

        