#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

def es_solucion(parcial, n):
    # Verifica si la solución parcial tiene el tamaño adecuado
    return len(parcial) == n


def es_valida(parcial):
    # Verifica si la solución parcial cumple con las restricciones
    # En este ejemplo, asumimos que cualquier solución parcial es válida
    return True


def backtracking(parcial, n):
    if es_solucion(parcial, n):
        return parcial

    for candidato in range(1, n+1):
        parcial.append(candidato)

        if es_valida(parcial):
            solucion = backtracking(parcial, n)
            if solucion:
                return solucion

        parcial.pop()

    return None


# Ejemplo de uso
if __name__ == "__main__":
    n = 4  # Tamaño del problema
    solucion = backtracking([], n)

    if solucion:
        print("Solución encontrada:", solucion)
    else:
        print("No se encontró solución.")
        