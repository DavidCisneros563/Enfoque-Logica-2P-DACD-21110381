#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class ModalOperator:
    def __init__(self, proposition, modality):
        self.proposition = proposition
        self.modality = modality

    def __str__(self):
        return f"{self.modality}({self.proposition})"

class World:
    def __init__(self, propositions):
        self.propositions = propositions

    def evaluate(self, proposition):
        return proposition in self.propositions

class ModalLogicAgent:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def tell(self, modal_sentence):
        self.kb.append(modal_sentence)

    def ask(self, modal_query):
        for sentence in self.kb:
            if isinstance(sentence, ModalOperator) and sentence.modality == "necesario":
                if not self.evaluate_necessary(sentence.proposition):
                    return False
            elif isinstance(sentence, ModalOperator) and sentence.modality == "posible":
                if not self.evaluate_possible(sentence.proposition):
                    return False
        return True

    def evaluate_necessary(self, proposition):
        for world in self.worlds:
            if not world.evaluate(proposition):
                return False
        return True

    def evaluate_possible(self, proposition):
        for world in self.worlds:
            if world.evaluate(proposition):
                return True
        return False

# Ejemplo de uso
if __name__ == "__main__":
    # Definir mundos posibles con sus proposiciones
    world1 = World(["p", "q"])
    world2 = World(["p"])
    world3 = World(["q"])

    # Crear agentes con conocimiento
    agent1 = ModalLogicAgent([ModalOperator("p", "necesario")])
    agent2 = ModalLogicAgent([ModalOperator("p", "posible")])

    # Asignar los mundos a los agentes
    agent1.worlds = [world1, world2, world3]
    agent2.worlds = [world1, world2, world3]

    # Realizar consultas
    result1 = agent1.ask(ModalOperator("p", "necesario"))
    result2 = agent2.ask(ModalOperator("q", "posible"))

    # Mostrar resultados
    print("¿Es necesario que p? ", result1)
    print("¿Es posible que q? ", result2)
    