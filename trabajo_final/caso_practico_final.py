# Caso práctico final: Lista de tareas

class ListaTareas:
    def __init__(self):
        self.tareas = []  # Inicialización de la lista de tareas

    # Método para agregar una nueva tarea a la lista
    def agregar_tarea(self, tarea):
        if not tarea.strip():
            print("\nError: La tarea no puede estar vacía")
        else:
            self.tareas.append({"descripcion": tarea, "completada": False})
            print("\nLa tarea ha sido añadida.")

    # Método para marcar una tarea como completada
    def marcar_completada(self, posicion):
        try:
            self.tareas[posicion]["completada"] = True  # Marca la tarea en la posición dada como completada
            print("\nLa tarea ha sido completada.")
        except IndexError:
            print("\nError: La posición ingresada no es válida.")  # Manejo de excepción para posición inválida

    # Método para mostrar todas las tareas y su estado
    def mostrar_tareas(self):
        print("\nTareas:")
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea["completada"] else "Pendiente"  # Determina el estado de la tarea
            print(f"{i+1}. {tarea['descripcion']} - Estado: {estado}")  
        
    # Método para eliminar una tarea de la lista
    def eliminar_tarea(self, posicion):
        try:
            del self.tareas[posicion] 
            print("\nLa tarea ha sido eliminada.")
        except IndexError:
            print("\nError: La posición ingresada no es válida.")  # Manejo de excepción para posición inválida


# Función principal
def main():
    lista_tareas = ListaTareas() 

    while True:
        print("")
        print("\n--- MENU ---")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("0. Salir")

        opcion = input("Seleccione una opción: ") 

        if opcion == "1":
            tarea = input("Ingrese la nueva tarea: ")  
            lista_tareas.agregar_tarea(tarea)  # Llama al método para agregar la tarea
        elif opcion == "2":
            try:
                posicion = int(input("Ingrese la posición de la tarea a marcar como completada: ")) - 1
                lista_tareas.marcar_completada(posicion)  # Llama al método para marcar la tarea como completada
            except ValueError:
                print("\nError: La posición debe ser un número entero.")  # Manejo de excepción para posición no numérica
        elif opcion == "3":
            lista_tareas.mostrar_tareas()  # Llama al método para mostrar todas las tareas y su estado
        elif opcion == "4":
            try:
                posicion = int(input("Ingrese la posición de la tarea a eliminar: ")) - 1
                lista_tareas.eliminar_tarea(posicion)  # Llama al método para eliminar la tarea
            except ValueError:
                print("\nError: La posición debe ser un número entero.")  # Manejo de excepción para posición no numérica
        elif opcion == "0":
            print("Saliendo del programa...") 
            break  # Termina el bucle y sale del programa
        else:
            print("\nOpción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()