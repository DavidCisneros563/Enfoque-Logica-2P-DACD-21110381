#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class AQ:
    def __init__(self, concepto_positivo, concepto_negativo, atributos):
        self.positive_concept = concepto_positivo
        self.negative_concept = concepto_negativo
        self.attributes = atributos
        self.hypothesis = self.initialize_hypothesis()

    def initialize_hypothesis(self):
        hypothesis = {attr: 'dont care' for attr in self.attributes}
        return hypothesis

    def update_hypothesis(self, instance, label):
        if label == self.positive_concept:
            for attr, value in instance.items():
                if value != self.hypothesis[attr]:
                    self.hypothesis[attr] = 'dont care'
        elif label == self.negative_concept:
            for attr, value in instance.items():
                if value != self.hypothesis[attr]:
                    self.hypothesis[attr] = value

    def print_hypothesis(self):
        print("AQ Hypothesis:")
        print(self.hypothesis)

# Ejemplo de uso
attributes = ['outlook', 'temperature', 'humidity']
positive_concept = 'play'
negative_concept = 'not play'

aq = AQ(positive_concept, negative_concept, attributes)

instances = [
    {'outlook': 'sunny', 'temperature': 'hot', 'humidity': 'high', 'play': 'no'},
    {'outlook': 'overcast', 'temperature': 'mild', 'humidity': 'normal', 'play': 'yes'},
    {'outlook': 'rainy', 'temperature': 'cool', 'humidity': 'normal', 'play': 'yes'},
    {'outlook': 'sunny', 'temperature': 'hot', 'humidity': 'normal', 'play': 'yes'},
]

# Entrenamiento de AQ
for instance in instances:
    aq.update_hypothesis(instance, instance[positive_concept])

# Imprimir hipótesis
aq.print_hypothesis()
