#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import heapq

class Nodo:
    def __init__(self, estado, costo_camino, heuristica):
        self.estado = estado
        self.costo_camino = costo_camino
        self.heuristica = heuristica

    def __lt__(self, otro):
        return (self.costo_camino + self.heuristica) < (otro.costo_camino + otro.heuristica)

def a_estrella(estado_inicial, es_objetivo, sucesores, heuristica):
    frontera = []
    heapq.heappush(frontera, Nodo(estado_inicial, 0, heuristica(estado_inicial)))
    visitados = set()

    while frontera:
        nodo_actual = heapq.heappop(frontera)
        estado_actual, costo_camino_actual = nodo_actual.estado, nodo_actual.costo_camino

        if es_objetivo(estado_actual):
            return estado_actual

        if estado_actual in visitados:
            continue
        visitados.add(estado_actual)

        for accion, estado_siguiente, costo in sucesores(estado_actual):
            if estado_siguiente not in visitados:
                nueva_carga_camino = costo_camino_actual + costo
                heapq.heappush(frontera, Nodo(estado_siguiente, nueva_carga_camino, heuristica(estado_siguiente)))

    return None

# Ejemplo de uso
def es_objetivo(estado):
    return estado == "F"

def sucesores(estado):
    if estado == "A":
        return [("Mover a B", "B", 5), ("Mover a C", "C", 3)]
    elif estado == "B":
        return [("Mover a F", "F", 10)]
    elif estado == "C":
        return [("Mover a D", "D", 7)]
    elif estado == "D":
        return [("Mover a F", "F", 2)]

def heuristica(estado):
    return {
        "A": 10,
        "B": 5,
        "C": 8,
        "D": 3,
        "F": 0
    }[estado]

resultado = a_estrella("A", es_objetivo, sucesores, heuristica)
print("Planificación completa:", resultado)