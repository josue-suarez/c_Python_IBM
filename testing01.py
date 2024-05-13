from math import pi
def area(r):
    area_c = pi*(r**2)
    return area_c

valores = [1, 3, 0, -1, -3, 2+3j, True, "hola"]

for v in valores:
    area_calculada = area(v)
    print(f"Para el valor {v} el área es: {area_calculada}")
    