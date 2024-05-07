#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial


class KnowledgeBase:
    def __init__(self):
        self.knowledge = set()

    def tell(self, sentence):
        self.knowledge.add(sentence)

    def ask(self, query):
        return query in self.knowledge

class LogicalAgent:
    def __init__(self):
        self.kb = KnowledgeBase()

    def perceive(self, percept):
        # Percibir el entorno y actualizar la base de conocimientos
        self.kb.tell(percept)

    def act(self):
        # Tomar decisiones basadas en el conocimiento
        if self.kb.ask("llueve"):
            print("Llevar un paraguas")
        else:
            print("No llevar un paraguas")

# Ejemplo de uso
if __name__ == "__main__":
    agent = LogicalAgent()

    # Percepción del entorno
    agent.perceive("llueve")

    # Toma de decisiones
    agent.act()