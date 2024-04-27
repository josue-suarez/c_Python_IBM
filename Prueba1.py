# Solicitamos nombre y edad al usuario
nombre = input("introduzca su nombre: ")
edad = int(input("introduzca s edad: "))

# Comnprobamos si es mayor de edad, y además, si está casado
casado = False
print(f"Bienvenido {nombre}")
if edad >= 18 and casado:
    print("Eres mayor de edad y estás soltero")
elif edad >= 18 and not casado:
    print("Eres mayor de edad y estás casado")
else:
    print("No eres mayor de edad")
