#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

# Razonamiento Deductivo
def razonamiento_deductivo():
    # Conocimiento
    premisa_1 = "Todos los hombres son mortales."
    premisa_2 = "Sócrates es un hombre."

    # Inferencia
    if premisa_1.endswith("mortales") and premisa_2.endswith("hombre"):
        conclusion = "Sócrates es mortal."
    else:
        conclusion = "No se puede inferir la mortalidad de Sócrates."

    return conclusion

# Razonamiento Inductivo
def razonamiento_inductivo(datos):
    # Observaciones
    observacion_1 = datos["observacion_1"]
    observacion_2 = datos["observacion_2"]
    observacion_3 = datos["observacion_3"]

    # Patrón de generalización
    if observacion_1 == observacion_2 == observacion_3:
        generalizacion = "Todas las observaciones tienen el mismo resultado."
    else:
        generalizacion = "No hay un patrón claro en las observaciones."

    return generalizacion

# Aprendizaje Supervisado
def aprendizaje_supervisado(datos_entrenamiento):
    # Datos de entrenamiento: (entrada, salida)
    ejemplos = datos_entrenamiento["ejemplos"]

    # Modelo: Clasificador lineal simple
    def clasificador_lineal(entrada):
        if entrada < 5:
            return "Clase A"
        else:
            return "Clase B"

    # Entrenamiento y evaluación
    precision = sum(1 for entrada, salida_esperada in ejemplos if clasificador_lineal(entrada) == salida_esperada) / len(ejemplos)

    return precision

# Aprendizaje No Supervisado
def aprendizaje_no_supervisado(datos_no_etiquetados):
    # Datos no etiquetados
    datos = datos_no_etiquetados["datos"]

    # Modelo: Algoritmo de agrupamiento (Clustering)
    grupos = {}  # Aquí deberíamos tener grupos identificados por el algoritmo de agrupamiento

    return grupos

# Ejemplo de uso
if __name__ == "__main__":
    # Datos para razonamiento inductivo
    datos_inductivos = {
        "observacion_1": "A",
        "observacion_2": "B",
        "observacion_3": "A"
    }

    # Datos para aprendizaje supervisado
    datos_entrenamiento = {
        "ejemplos": [(3, "Clase A"), (7, "Clase B"), (1, "Clase A"), (10, "Clase B")]
    }

    # Datos para aprendizaje no supervisado
    datos_no_etiquetados = {
        "datos": [5, 2, 8, 4, 7, 1]
    }

    # Realizar razonamiento y aprendizaje
    print("Razonamiento Deductivo:", razonamiento_deductivo())
    print("Razonamiento Inductivo:", razonamiento_inductivo(datos_inductivos))
    print("Aprendizaje Supervisado - Precisión:", aprendizaje_supervisado(datos_entrenamiento))
    print("Aprendizaje No Supervisado - Grupos:", aprendizaje_no_supervisado(datos_no_etiquetados))
    