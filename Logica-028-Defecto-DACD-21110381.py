#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class DefaultLogicBase:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def query(self, fact):
        for rule in self.rules:
            if rule.implies(fact):
                return True
        return False

class DefaultRule:
    def __init__(self, condition, consequence, default_consequence):
        self.condition = condition
        self.consequence = consequence
        self.default_consequence = default_consequence

    def implies(self, fact):
        return self.condition == fact

    def default_implies(self):
        return self.default_consequence

# Ejemplo de uso
if __name__ == "__main__":
    db = DefaultLogicBase()

    # Agregar reglas a la base de conocimientos
    db.add_rule(DefaultRule("p", "q", "r"))
    db.add_rule(DefaultRule("s", "t", "u"))

    # Consultar la base de conocimientos
    result1 = db.query("p")
    result2 = db.query("s")
    result3 = db.query("q")
    result4 = db.query("r")
    result5 = db.query("t")
    result6 = db.query("u")

    # Mostrar resultados
    print("¿Se sigue q a partir de p? ", result1)
    print("¿Se sigue t a partir de s? ", result2)
    print("¿Se sigue q? ", result3)
    print("¿Se sigue r? ", result4)
    print("¿Se sigue t? ", result5)
    print("¿Se sigue u? ", result6)
    