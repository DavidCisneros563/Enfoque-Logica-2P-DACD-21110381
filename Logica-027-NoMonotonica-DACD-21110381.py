#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class DefaultKnowledgeBase:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def query(self, fact):
        for rule in self.rules:
            if rule.implies(fact):
                return True
        return False

class Rule:
    def __init__(self, condition, consequence):
        self.condition = condition
        self.consequence = consequence

    def implies(self, fact):
        return self.condition == fact

# Ejemplo de uso
if __name__ == "__main__":
    kb = DefaultKnowledgeBase()

    # Agregar reglas a la base de conocimientos
    kb.add_rule(Rule("p", "q"))
    kb.add_rule(Rule("r", "s"))

    # Consultar la base de conocimientos
    result1 = kb.query("p")
    result2 = kb.query("r")
    result3 = kb.query("q")
    result4 = kb.query("s")

    # Mostrar resultados
    print("¿Se sigue q a partir de p? ", result1)
    print("¿Se sigue s a partir de r? ", result2)
    print("¿Se sigue q? ", result3)
    print("¿Se sigue s? ", result4)
    