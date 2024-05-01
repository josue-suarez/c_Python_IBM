class Usuario():  # Administador
    def __init__(self):
        self.nombre = "Ángel"
        self.edad = 47
        self.login = "admin"
        self.password = "1234"
        self.email = "angel@email.com"
        self.telefono = 666666666


    def resumen(self):
        print(f"Los datos del usuario son:\n"
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad}\n"
            f"Login: {self.login}\n"
            f"Password: {self.password}\n"
            f"Email: {self.email}\n"
            f"Teléfono: {self.telefono}")
    
    def cambiaEdad(self):
        edad_Introducida = int(input("Introduzca edad entre 18-100:"))

        if 18 < edad_Introducida < 100:
            self.edad = edad_Introducida
            print("Edad introducida correcta.")
            return ""
        else:
            print("Edad introducida no correcta.")
            self.cambiaEdad()
            return ""
        
    def muestraEdad(self):
            print("La edad del usuario es:", self.edad, "anios.")
            return ""

    def __del__(self):
         print("Objeto eliminado.")

# Crear instancia administrador 
administrador = Usuario()

# Usar programa - Aplicar métodos
administrador.resumen()
administrador.cambiaEdad()
administrador.muestraEdad()
# del administrador - elimina instancia administrador