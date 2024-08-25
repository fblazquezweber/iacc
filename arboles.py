class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.derecho = None
        self.izquierdo = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo
        else:
            aux = self.raiz
            while aux is not None:
                if aux.valor <= nuevo.valor:
                    if aux.derecho is None:
                        aux.derecho = nuevo
                        break
                    else:
                        aux = aux.derecho
                else:
                    if aux.izquierdo is None:
                        aux.izquierdo = nuevo
                        break
                    else:
                        aux = aux.izquierdo

    def busqueda(self, valor):
        if self.raiz is None:
            print("Arbol sin elementos")
        else:
            aux = self.raiz
            while aux is not None:
                if aux.valor == valor:
                    print(f"Exito se encontro el valor {aux.valor} en {aux}")
                    return
                else:
                    if aux.valor < valor:
                        aux = aux.derecho
                    else:
                        aux = aux.izquierdo
            print("Valor no encontrado")

    def inorden(self):
        self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo)  # Recorre el subárbol izquierdo
            print(nodo.valor)  # Procesa el nodo actual
            self._inorden_recursivo(nodo.derecho)





arbol = Arbol()
arbol.insertar(100)
arbol.insertar(200)
arbol.insertar(50)
arbol.insertar(150)
arbol.insertar(75)
arbol.insertar(80)
arbol.insertar(70)
arbol.insertar(45)
arbol.insertar(180)
arbol.insertar(300)
arbol.insertar(300)

arbol.inorden()
#arbol.busqueda(300)
#print(arbol.raiz)
#print(arbol.raiz.valor)
#print(arbol.raiz.derecho.valor)
#print("Valor: ",arbol.raiz.derecho.derecho.valor, "Memoria",arbol.raiz.derecho.derecho)
#print("Valor: ",arbol.raiz.derecho.derecho.derecho.valor,"Memoria", arbol.raiz.derecho.derecho.derecho)

#print(arbol.raiz.derecho.izquierdo.valor)
#print(arbol.raiz.derecho.izquierdo.derecho.valor)
#print(arbol.raiz.izquierdo.valor)
#print(arbol.raiz.izquierdo.izquierdo.valor)
#print(arbol.raiz.izquierdo.derecho.valor)
#print(arbol.raiz.izquierdo.derecho.izquierdo.valor)
#print(arbol.raiz.izquierdo.derecho.derecho.valor)
#print(arbol.raiz.izquierdo.derecho.derecho.derecho)
#print(arbol.raiz.izquierdo.derecho.derecho.izquierdo)




