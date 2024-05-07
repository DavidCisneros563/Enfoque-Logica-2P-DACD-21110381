#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import random


def funcion_objetivo(solucion):
    # En este ejemplo, la función objetivo es la suma de los elementos de la solución
    return sum(solucion)


def generar_vecino(solucion_actual):
    # Genera un vecino cambiando aleatoriamente un elemento de la solución actual
    vecino = solucion_actual[:]
    indice = random.randint(0, len(vecino)-1)
    vecino[indice] = 1 - vecino[indice]  # Cambia de 0 a 1 o de 1 a 0
    return vecino


def hill_climbing(solucion_inicial, max_iter):
    solucion_actual = solucion_inicial
    valor_actual = funcion_objetivo(solucion_actual)

    for _ in range(max_iter):
        vecino = generar_vecino(solucion_actual)
        valor_vecino = funcion_objetivo(vecino)

        if valor_vecino >= valor_actual:
            solucion_actual = vecino
            valor_actual = valor_vecino

    return solucion_actual, valor_actual


# Ejemplo de uso
if __name__ == "__main__":
    solucion_inicial = [random.randint(0, 1) for _ in range(10)]  # Genera una solución inicial aleatoria
    max_iter = 100  # Número máximo de iteraciones

    solucion_final, valor_final = hill_climbing(solucion_inicial, max_iter)
    print("Solución final encontrada:", solucion_final)
    print("Valor de la función objetivo:", valor_final)