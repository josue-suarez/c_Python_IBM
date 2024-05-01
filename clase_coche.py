# Declaración clase
class Coche():

# Declaración atributos - En común todos los objetos de la clase
# Constructor
    def __init__(self):
        largo = 250
        ancho = 120
        ruedas = 4
        peso = 900
        color = "rojo"
        is_enmarcha = False
    
# Declaración métodos [Arrancar, Estado]
    def arrancar(self):  # self instancia de clase
        self.is_enmarcha = True  # Es igual a miCoche.is_enmarcha = True

    def estado(self):
        if (self.is_enmarcha == True):
            print("Coche arrancado")
        else:
            print("Coche no arrancado")

# Declaración instancias u objetos de clase

miCoche = Coche()
miCoche2 = Coche()

# Acceso a atributo de clase Coche
print("El largo de miCoche es:", miCoche.largo, "cm")
print("Número de ruedas de miCoche:", miCoche.ruedas)

#Acceso a método de clase Coche
print("*Arrancamos miCoche*")
miCoche.arrancar()
miCoche.estado()

