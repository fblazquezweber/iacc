class Nodo:
    def __init__(self, tarea, nivel, estado, fecha):
        self.tarea = tarea
        self.nivel = nivel
        self.estado = estado
        self.fecha = fecha
        self.next = None
        self.back = None

class Lista:
    def __init__(self):
        self.cabeza = None
        self.cola =  None

    def agregarCabeza(self, tarea, nivel, estado, fecha):
        nuevaTarea = Nodo(tarea, nivel, estado, fecha)
        if self.cabeza is None:
            self.cabeza = nuevaTarea
            self.cola = nuevaTarea
        else:
            nuevaTarea.next = self.cabeza
            self.cabeza.back = nuevaTarea
            self.cabeza = nuevaTarea

    def agregarCola(self, tarea, nivel, estado, fecha):
        nuevaTarea = Nodo(tarea, nivel, estado, fecha)
        if self.cabeza is None:
            self.cabeza = nuevaTarea
            self.cola = nuevaTarea
        else:
            self.cola.next = nuevaTarea
            nuevaTarea.back = self.cola
            self.cola = nuevaTarea

    def eliminar(self, estado):
        encontrado = False
        if self.cabeza is None:
            print("La lista esta vacía")
        else:
            aux = self.cabeza
            while aux is not None:
                if aux.estado == estado:
                    encontrado = True
                    print(f"La {aux.tarea} se encuentra {aux.estado} desde {aux.fecha}")
                    decision = input("¿Desea eliminar esta tarea? (s/n): ")
                    if decision.lower() == 's':
                        if aux == self.cabeza and aux == self.cola:
                            self.cabeza = None
                            self.cola = None
                        elif aux == self.cabeza:
                            self.cabeza = aux.next
                            aux.next.back = None
                        elif aux == self.cola:
                            self.cola = aux.back
                            aux.back.next = None
                        else:
                            aux.back.next = aux.next
                            aux.next.back = aux.back
                        print(f"Se ha eliminado la tarea {aux.tarea} {aux.estado} desde {aux.fecha}")
                    else:
                        print("No se eliminó la tarea.")
                aux = aux.next
            if not encontrado:
                print(f"No se encontraron tareas con el estado '{estado}'.")

    def busqueda(self, estado):
        aux = self.cabeza
        encontrado = False
        if self.cabeza is None:
            print("La lista esta vacia")
        else:
            while aux is not None:
                if aux.estado == estado:
                    print(f"La {aux.tarea} se encuentra {aux.estado} desde {aux.fecha}")
                    encontrado = True
                aux = aux.next
            if not encontrado:
                print(f"No se encontraron tareas con el estado '{estado}'.")

    def actualizar(self, tarea):
        aux = self.cabeza
        encontrado = False
        if self.cabeza == None:
            print("La lista esta vacia")
        else:
            while aux is not None:
                if aux.tarea == tarea:
                    encontrado = True
                    print(f"La tarea {aux.tarea} está en estado '{aux.estado}' desde {aux.fecha}")
                    print("¿Desea cambiar el estado de esta tarea?")
                    print("1. Pendiente")
                    print("2. En Progreso")
                    print("3. Completada")
                    print("4. No cambiar")
                    opcion = int(input("Seleccione una opción para cambiar el estado o 'No cambiar' para mantenerlo: "))
                    nuevo_estado = ["Pendiente", "En Progreso", "Completada"]
                    if opcion in [1, 2, 3]:
                        aux.estado = nuevo_estado[opcion-1]
                        print(f"Estado actualizado: La tarea {aux.tarea} ahora está '{aux.estado}'.")
                    elif opcion == 4:
                        print("No se realizaron cambios.")
                    else:
                        print("Opción no válida. No se realizaron cambios.")
                aux = aux.next
            if not encontrado:
                print(f"No se encontraron tareas de '{tarea}'.")

    def mostrarTodo(self):
        if self.cabeza is None:
            print("La lista esta vacia")
        else:
            aux = self.cabeza
            while aux is not None:
                print(f"tarea: {aux.tarea} nivel: {aux.nivel} estado: {aux.estado} fecha: {aux.fecha}")
                aux = aux.next

    def eliminarTodo(self):
        self.cabeza = None
        self.cola = None

opcionesMenu = ["Agregar al inicio",
                "Agregar al final",
                "Eliminar",
                "Buscar estado",
                "Actualizar tarea",
                "Mostrar todas las tareas",
                "Eliminar todo",
                "Salir"]

def mostrar_menu():
    print("-----Menú opciones-----")
    for i, opcion in enumerate(opcionesMenu, start=1):
        print(f"{i}. {opcion}")
    print("-----------------------")

lista = Lista()
while True:
    mostrar_menu()
    seleccion = int(input("Selecciones una opcion: "))
    if seleccion == 1:
        lista.agregarCabeza(
            input("Ingrese el nombre de la tarea: "),
            input("Ingrese el nivel: "),
            input("Ingrese el estado: "),
            input("Ingrese la fecha: ")
        )
    elif seleccion == 2:
        lista.agregarCola(
            input("Ingrese el nombre de la tarea: "),
            input("Ingrese el nivel: "),
            input("Ingrese el estado: "),
            input("Ingrese la fecha: ")
        )
    elif seleccion == 3:
        lista.eliminar(input("Indique el estado de la tarea a eliminar: "))
    elif seleccion == 4:
        lista.busqueda(input("Indique el estado de la tarea a buscar: "))
    elif seleccion == 5:
        lista.actualizar(input("Indique la tarea a actualizar: "))
    elif seleccion == 6:
        lista.mostrarTodo()
    elif seleccion == 7:
        lista.eliminarTodo()
    elif seleccion == 8:
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
