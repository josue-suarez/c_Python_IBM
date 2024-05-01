# Crear clase padre Vehiculo
class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "Negro"
        self.arrancado = False
        self.parado = True
    
    def arrancar(self):
        self.arrancado = True
        self.parado = False
    
    def parrar(self):
        self.arrancado = False
        self.parado = True
            
    def resumen(self):
        print(f"""Estado del vehículo: 
              Marca: {self.marca} 
              Modelo: {self.modelo} 
              Color: {self.color} 
              Arrancado: {self.arrancado}""")

# Crear instancia miCoche de clase padre Vehiculo
miCoche = Vehiculo("Renault", "Megane")

# Utilizar métodos comunes
miCoche.arrancar()
miCoche.resumen()

# Crear clase Moto que hereda de clase padre Vehiculo
class Moto(Vehiculo):
    is_carenado = False
    def poner_carenado(self):  # Método propio de la clase Moto, no heredado
        self.is_carenado = True
    def resumen(self):
        print(f"""Estado del vehículo: 
              Marca: {self.marca} 
              Modelo: {self.modelo} 
              Color: {self.color} 
              Arrancado: {self.arrancado}
              Carenado: {self.is_carenado}""")

# Crear instancia miMoto de clase padre Moto, que hereda de clase padre Vehiculo
miMoto = Moto("Kawasaki", "Ninja")

# Utilizar métodos
miMoto.color = "Rojo"
miMoto.poner_carenado()
miMoto.arrancar()
miMoto.resumen()

# Crear clase Quad que herede de clase padre Moto, a su vez de clase padre Vehiculo
class Quad(Moto):
    pass

# Crear instancia de clase Quad
miQuad = Quad("Honda", "Q")

miQuad.color = "Verde"
miQuad.arrancar()
miQuad.resumen()
