# Solicitamos nombre y edad al usuario
nombre = input("introduzca su nombre: ")
edad = int(input("introduzca su edad: "))

# Comnprobamos si está casado
while True:
    casado = input("Indique si está casado [C] o soltero [S]: ")
    if casado.upper() == "C":
        casado = True
        break
    elif casado.upper() == "S":
        casado = False
        break
    else:
        print("""Opción no válida.
            Indique C si está casado,
            o S si está soltero. """)

# Mostramos informacón en pantalla
print(f"Bienvenido {nombre}")
if edad >= 18 and not casado:
    print("Eres mayor de edad y estás soltero")
elif edad >= 18 and casado:
    print("Eres mayor de edad y estás casado")
elif edad < 18 and not casado:
    print("No eres mayor de edad y estás soltero")
else:
    print("No eres mayor de edad y estás casado")
