#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

class NodoDecision:
    def __init__(self, atributo=None, valor=None, hijos=None, clase=None):
        self.atributo = atributo  # Atributo en el que se divide este nodo
        self.valor = valor  # Valor del atributo en el que se divide este nodo
        self.hijos = hijos or {}  # Diccionario de hijos (valor del atributo -> NodoDecision)
        self.clase = clase  # Clase asignada si este nodo es una hoja

def calcular_entropia(etiquetas):
    clases, conteos = np.unique(etiquetas, return_counts=True)
    entropia = np.sum([(-conteos[i] / np.sum(conteos)) * np.log2(conteos[i] / np.sum(conteos)) for i in range(len(clases))])
    return entropia

def dividir_datos(datos, atributo_divisor, valor_divisor):
    indices = np.where(datos[:, atributo_divisor] == valor_divisor)[0]
    return np.delete(datos, atributo_divisor, axis=1)[indices]

def id3(datos, etiquetas, atributos):
    if len(np.unique(etiquetas)) <= 1:
        return NodoDecision(clase=etiquetas[0])

    if len(atributos) == 0:
        clase_mas_comun = np.argmax(np.bincount(etiquetas))
        return NodoDecision(clase=clase_mas_comun)

    mejor_atributo = None
    mejor_ganancia_informacion = -1

    entropia_padre = calcular_entropia(etiquetas)

    for atributo in atributos:
        valores = np.unique(datos[:, atributo])
        ganancia_informacion = entropia_padre
        for valor in valores:
            datos_divididos = dividir_datos(datos, atributo, valor)
            etiquetas_divididas = etiquetas[datos[:, atributo] == valor]
            probabilidad = len(etiquetas_divididas) / len(etiquetas)
            ganancia_informacion -= probabilidad * calcular_entropia(etiquetas_divididas)
        if ganancia_informacion > mejor_ganancia_informacion:
            mejor_ganancia_informacion = ganancia_informacion
            mejor_atributo = atributo

    nodos_hijos = {}
    for valor in np.unique(datos[:, mejor_atributo]):
        datos_divididos = dividir_datos(datos, mejor_atributo, valor)
        etiquetas_divididas = etiquetas[datos[:, mejor_atributo] == valor]
        atributos_restantes = [a for a in atributos if a != mejor_atributo]
        nodos_hijos[valor] = id3(datos_divididos, etiquetas_divididas, atributos_restantes)

    return NodoDecision(atributo=mejor_atributo, valor=None, hijos=nodos_hijos)

def predecir(instancia, arbol):
    if arbol.clase is not None:
        return arbol.clase
    atributo = instancia[arbol.atributo]
    if atributo not in arbol.hijos:
        return None  # Valor no visto durante el entrenamiento
    return predecir(instancia, arbol.hijos[atributo])

# Ejemplo de uso
datos_entrenamiento = np.array([
    [1, 'sol', 'calor', 'no'],
    [2, 'sol', 'calor', 'no'],
    [3, 'nublado', 'calor', 'si'],
    [4, 'lluvia', 'templado', 'si'],
    [5, 'lluvia', 'frio', 'si'],
    [6, 'lluvia', 'frio', 'no'],
    [7, 'nublado', 'frio', 'si'],
    [8, 'sol', 'templado', 'no'],
    [9, 'sol', 'frio', 'si'],
    [10, 'lluvia', 'templado', 'si']
])

atributos = [0, 1, 2]  # Índices de los atributos en los datos (0-indexed)
etiquetas = datos_entrenamiento[:, -1]  # Última columna de los datos como etiquetas

arbol = id3(datos_entrenamiento, etiquetas, atributos)

# Ejemplo de predicción
instancia = [11, 'sol', 'calor']
print("Predicción para la instancia:", instancia)
print("Resultado:", predecir(instancia, arbol))
