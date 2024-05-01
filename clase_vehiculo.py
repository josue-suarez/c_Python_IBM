class Vehiculo():
    def __init__(self):
        marca = ""
        modelo = ""
        color = "negro"
        is_arrancado = False
        is_parado = True
    
    def arrancar():
        if is_arrancado == False:
            is_arrancado = True
            is_parado = False
            print("Vehículo se ha arrancado.")
            return ""
        else:
            print("Vehículo ya está arrancado")
    
    def parrar():
        if is_arrancado == True:
            is_arrancado = False
            is_parado = True
            print("vehículo se ha parado.")
            return ""
        else:
            print("Vehículo ya está parado")
    
    def resumen():
        print("Estado del vehículo:\n"
            f"Marca: {self.marca}"
            f"Modelo: {self.modelo}
            f"Color: {self.color}"
            f"Arrancado: {self.is_arrancado}")
        