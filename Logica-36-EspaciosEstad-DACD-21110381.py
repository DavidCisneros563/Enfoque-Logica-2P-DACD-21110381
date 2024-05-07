#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from queue import Queue

class Laberinto:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])

    def es_valido(self, fila, columna):
        return 0 <= fila < self.filas and 0 <= columna < self.columnas and self.laberinto[fila][columna] != '#'

    def es_meta(self, fila, columna):
        return fila == self.filas - 1 and columna == self.columnas - 1

    def encontrar_camino(self, inicio):
        movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Abajo, Arriba, Derecha, Izquierda
        visitados = set()
        cola = Queue()
        cola.put((inicio, []))  # (coordenadas, camino)

        while not cola.empty():
            (fila, columna), camino = cola.get()
            if self.es_meta(fila, columna):
                return camino + [(fila, columna)]
            for df, dc in movimientos:
                nueva_fila, nueva_columna = fila + df, columna + dc
                if self.es_valido(nueva_fila, nueva_columna) and (nueva_fila, nueva_columna) not in visitados:
                    cola.put(((nueva_fila, nueva_columna), camino + [(fila, columna)]))
                    visitados.add((nueva_fila, nueva_columna))

        return None

laberinto = [
    ['#', '.', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.'],
    ['#', '#', '#', '#', '#', '#']
]

lab = Laberinto(laberinto)
inicio = (0, 0)
camino = lab.encontrar_camino(inicio)

if camino:
    print("Camino encontrado:")
    for fila, columna in camino:
        print(f"({fila}, {columna})")
else:
    print("No se encontró un camino válido.")