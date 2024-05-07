#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion

class KnowledgeBase:
    def __init__(self, rules):
        self.rules = rules

    def forward_chain(self, facts):
        while True:
            new_facts = []
            for rule in self.rules:
                if all(condition in facts for condition in rule.conditions) and rule.conclusion not in facts:
                    new_facts.append(rule.conclusion)
            if not new_facts:
                break
            facts += new_facts
        return facts

    def backward_chain(self, goal, facts):
        if goal in facts:
            return True
        for rule in self.rules:
            if rule.conclusion == goal:
                if all(self.backward_chain(condition, facts) for condition in rule.conditions):
                    return True
        return False

# Ejemplo de uso
if __name__ == "__main__":
    rules = [
        Rule(["P", "Q"], "R"),
        Rule(["S"], "P"),
        Rule(["T"], "Q"),
        Rule(["S"], "T")
    ]

    kb = KnowledgeBase(rules)

    facts = ["S"]
    goal = "R"

    print("Encadenamiento hacia adelante:")
    inferred_facts_forward = kb.forward_chain(facts)
    print("Hechos inferidos:", inferred_facts_forward)

    print("\nEncadenamiento hacia atrás:")
    result_backward = kb.backward_chain(goal, facts)
    print("¿Se puede inferir R a partir de los hechos? ", result_backward)
    