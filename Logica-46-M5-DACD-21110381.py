#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

class NodoRegresion:
    def __init__(self, atributo=None, valor=None, hijos=None, predicciones=None):
        self.atributo = atributo  # Atributo en el que se divide este nodo
        self.valor = valor  # Valor del atributo en el que se divide este nodo
        self.hijos = hijos or {}  # Diccionario de hijos (valor del atributo -> NodoRegresion)
        self.predicciones = predicciones  # Predicciones si este nodo es una hoja

def calcular_error_cuadratico_medio(predicciones, etiquetas):
    return np.mean((predicciones - etiquetas) ** 2)

def dividir_datos(datos, etiquetas, atributo_divisor, valor_divisor):
    indices = np.where(datos[:, atributo_divisor] == valor_divisor)[0]
    return datos[indices], etiquetas[indices]

def m5(datos, etiquetas, atributos, min_instancias, min_error):
    if len(datos) <= min_instancias or len(np.unique(etiquetas)) == 1:
        return NodoRegresion(predicciones=np.mean(etiquetas))

    error_padre = calcular_error_cuadratico_medio(etiquetas, np.mean(etiquetas))

    mejor_atributo = None
    mejor_valor_divisor = None
    mejor_error_division = float('inf')
    mejor_predicciones = None

    for atributo in atributos:
        valores = np.unique(datos[:, atributo])
        for valor in valores:
            datos_divididos, etiquetas_divididas = dividir_datos(datos, etiquetas, atributo, valor)
            error_division = calcular_error_cuadratico_medio(etiquetas_divididas, np.mean(etiquetas_divididas))
            if error_division < mejor_error_division:
                mejor_atributo = atributo
                mejor_valor_divisor = valor
                mejor_error_division = error_division
                mejor_predicciones = np.mean(etiquetas_divididas)

    if error_padre - mejor_error_division < min_error:
        return NodoRegresion(predicciones=np.mean(etiquetas))

    nodos_hijos = {}
    datos_divididos, etiquetas_divididas = dividir_datos(datos, etiquetas, mejor_atributo, mejor_valor_divisor)
    atributos_restantes = [a for a in atributos if a != mejor_atributo]
    nodos_hijos[mejor_valor_divisor] = m5(datos_divididos, etiquetas_divididas, atributos_restantes, min_instancias, min_error)

    return NodoRegresion(atributo=mejor_atributo, valor=mejor_valor_divisor, hijos=nodos_hijos)

def predecir(instancia, arbol):
    if arbol.predicciones is not None:
        return arbol.predicciones
    atributo = instancia[arbol.atributo]
    if atributo not in arbol.hijos:
        return None  # Valor no visto durante el entrenamiento
    return predecir(instancia, arbol.hijos[atributo])

# Ejemplo de uso
datos_entrenamiento = np.array([
    [1, 3, 4],
    [2, 5, 8],
    [3, 4, 6],
    [4, 7, 10],
    [5, 2, 3],
    [6, 1, 2]
])

etiquetas_entrenamiento = np.array([5, 8, 10, 12, 4, 3])

atributos = [0, 1]  # Índices de los atributos en los datos (0-indexed)

arbol = m5(datos_entrenamiento, etiquetas_entrenamiento, atributos, min_instancias=2, min_error=0.1)

# Ejemplo de predicción
instancia = [7, 3]
print("Predicción para la instancia:", instancia)
print("Resultado:", predecir(instancia, arbol))
