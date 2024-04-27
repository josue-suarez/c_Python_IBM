nombre = "Andrés"
edad = 28
casado = False
print(f"Bienvenido {nombre}")
if edad >= 18 and casado == False:
    print("Eres mayor de edad y estás soltero")
elif edad >= 18 and casado == True:
    print("Eres mayor de edad y estás casado")
else:
    print("No eres mayor de edad")
