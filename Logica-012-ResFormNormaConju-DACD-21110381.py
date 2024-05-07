#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class Clausula:
    def __init__(self, literales):
        self.literales = set(literales)

    def __repr__(self):
        return " | ".join(self.literales)


def resolucion(cnf):
    nuevas_clausulas = set()
    while True:
        pares_clausulas = [(clausula1, clausula2) for clausula1 in cnf for clausula2 in cnf if clausula1 != clausula2]
        for clausula1, clausula2 in pares_clausulas:
            resolvente = clausula1.literales.symmetric_difference(clausula2.literales)
            if len(resolvente) == 2 and resolvente not in nuevas_clausulas:
                nuevas_clausulas.add(Clausula(resolvente))
        if nuevas_clausulas.issubset(cnf):
            return False
        if nuevas_clausulas.intersection(cnf):
            return True
        cnf.update(nuevas_clausulas)


def convertir_a_FNC(formula):
    # Aquí puedes agregar tu propio código para convertir la fórmula a FNC
    pass


# Ejemplo de uso
if __name__ == "__main__":
    # Supongamos que tenemos una fórmula en forma normal conjuntiva
    fnc = {Clausula({"p", "q", "~r"}), Clausula({"~p", "r"}), Clausula({"~q", "s"}), Clausula({"~s", "~p"})}

    # Verificamos la satisfacibilidad usando resolución
    satisfacible = resolucion(fnc)
    print("La fórmula es satisfacible:", satisfacible)

    # Supongamos que tenemos una fórmula que queremos convertir a FNC
    formula = "(p ∨ q) ∧ (p → r)"
    fnc_convertida = convertir_a_FNC(formula)
    print("Fórmula convertida a FNC:", fnc_convertida)