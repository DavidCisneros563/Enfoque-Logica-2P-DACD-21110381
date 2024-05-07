#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class Regla:
    def __init__(self, antecedentes, consecuente):
        self.antecedentes = antecedentes
        self.consecuente = consecuente

    def coincide(self, hechos):
        return all(antecedente in hechos for antecedente in self.antecedentes)


def encadenamiento_hacia_adelante(hechos, reglas):
    nuevos_hechos = set()
    activadas = True

    while activadas:
        activadas = False
        for regla in reglas:
            if regla.coincide(hechos) and regla.consecuente not in hechos:
                hechos.add(regla.consecuente)
                nuevos_hechos.add(regla.consecuente)
                activadas = True

    return nuevos_hechos


def encadenamiento_hacia_atras(hechos, reglas, meta):
    if meta in hechos:
        return True
    for regla in reglas:
        if regla.consecuente == meta:
            if all(encadenamiento_hacia_atras(hechos, reglas, antecedente) for antecedente in regla.antecedentes):
                return True
    return False


# Ejemplo de uso
if __name__ == "__main__":
    # Definición de reglas
    regla1 = Regla(["p", "q"], "r")
    regla2 = Regla(["s"], "p")
    regla3 = Regla(["r", "t"], "s")

    reglas = [regla1, regla2, regla3]

    # Encadenamiento hacia adelante
    hechos_adelante = {"p", "q", "t"}  # Hechos iniciales
    nuevos_hechos = encadenamiento_hacia_adelante(hechos_adelante, reglas)
    print("Hechos obtenidos mediante encadenamiento hacia adelante:", nuevos_hechos)

    # Encadenamiento hacia atrás
    hechos_atras = {"t"}  # Hechos iniciales
    meta = "r"  # Meta que queremos probar
    resultado_atras = encadenamiento_hacia_atras(hechos_atras, reglas, meta)
    print("¿La meta es alcanzable mediante encadenamiento hacia atrás?", resultado_atras)

