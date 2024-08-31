class Nodo:
    def __init__(self, distancia, vehiculo=None):
        self.distancia = distancia
        self.vehiculo = vehiculo
        self.derecha = None
        self.izquierda = None

class Vehiculo:
    def __init__(self, tipoCarga, cargaMax):
        self.tipoCarga = tipoCarga
        self.cargaMax = cargaMax

class Arbol:
    def __init__(self):
        self.raiz = Nodo(100)

    def insertar(self, distancia, vehiculo):
        nuevoNodo = Nodo(distancia, vehiculo)
        self.insertarRec(self.raiz, nuevoNodo)

    def insertarRec(self, nodo, nuevoNodo):
        if nuevoNodo.distancia < nodo.distancia:
            if nodo.izquierda is None:
                nodo.izquierda = nuevoNodo
            else:
                self.insertarRec(nodo.izquierda, nuevoNodo)
        elif nuevoNodo.distancia > nodo.distancia:
            if nodo.derecha is None:
                nodo.derecha = nuevoNodo
            else:
                self.insertarRec(nodo.derecha, nuevoNodo)

    def recorrerInorden(self, nodo):
        if nodo:
            self.recorrerInorden(nodo.izquierda)
            if nodo.vehiculo is not None:  # Solo imprimimos si el nodo tiene un vehículo asociado
                print(f"Ruta de {nodo.distancia} Km, "
                      f"Tipo de carga: {nodo.vehiculo.tipoCarga}, "
                      f"Capacidad de carga: {nodo.vehiculo.cargaMax} Kg")
            self.recorrerInorden(nodo.derecha)

    def generarInformeDetallado(self):
        print("Generando informe detallado de rutas:")
        self.recorrerInorden(self.raiz)

    def buscarRuta(self, distancia):
        nodo = self.buscarRec(self.raiz, distancia)
        if nodo:
            if nodo == self.raiz and nodo.vehiculo is None:
                print("Ruta encontrada: 100 Km, esta es la raíz del árbol, no tiene un vehículo asociado.")
            else:
                print(f"Ruta encontrada: {nodo.distancia} Km, "
                      f"Tipo de carga: {nodo.vehiculo.tipoCarga}, "
                      f"Carga máxima: {nodo.vehiculo.cargaMax} Kg")
        else:
            print("Ruta no encontrada.")
        return nodo

    def buscarRec(self, nodo, distancia):
        if nodo is None:
            return None
        if nodo.distancia == distancia:
            return nodo
        elif distancia < nodo.distancia:
            return self.buscarRec(nodo.izquierda, distancia)
        else:
            return self.buscarRec(nodo.derecha, distancia)

    def eliminar(self, distancia):
        if distancia == 100:
            print("No se puede eliminar la raíz inicial del árbol con distancia 100.")
            return
        nodo = self.buscarRec(self.raiz, distancia)
        if nodo is None:
            print(f"Ruta de {distancia} Km no encontrada en el árbol.")
        else:
            self.raiz = self.eliminarRec(self.raiz, distancia)
            print(f"Ruta de {distancia} Km eliminada del árbol.")

    def eliminarRec(self, nodo, distancia):
        if nodo is None:
            return nodo
        if distancia < nodo.distancia:
            nodo.izquierda = self.eliminarRec(nodo.izquierda, distancia)
        elif distancia > nodo.distancia:
            nodo.derecha = self.eliminarRec(nodo.derecha, distancia)
        else:
            #Caso 1: Sin hijos
            if nodo.izquierda is None and nodo.derecha is None:
                return None
            #Caso 2: Un solo hijo
            elif nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            #Caso 3: Dos hijos
            else:
                sucesor = self.encontrarMinimo(nodo.derecha)
                nodo.distancia = sucesor.distancia
                nodo.vehiculo = sucesor.vehiculo
                nodo.derecha = self.eliminarRec(nodo.derecha, sucesor.distancia)
        return nodo

    def encontrarMinimo(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo

arbol = Arbol()
arbol.insertar(80, Vehiculo('No perecedero', 2500))
arbol.insertar(75, Vehiculo('Perecedero', 500))
arbol.insertar(50, Vehiculo('No perecedero', 1500))
arbol.insertar(150, Vehiculo('Peligroso', 1000))
arbol.buscarRuta(75)
arbol.eliminar(75)
arbol.generarInformeDetallado()
