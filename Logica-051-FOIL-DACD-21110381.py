#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from collections import defaultdict
from impyla.foil import Foil
from impyla.predicate import Predicate

# Datos de ejemplo (ejemplos etiquetados)
datos = [
    {'outlook': 'sunny', 'temperature': 'hot', 'humidity': 'high', 'play': 'no'},
    {'outlook': 'overcast', 'temperature': 'mild', 'humidity': 'normal', 'play': 'yes'},
    {'outlook': 'rainy', 'temperature': 'cool', 'humidity': 'normal', 'play': 'yes'},
    {'outlook': 'sunny', 'temperature': 'hot', 'humidity': 'normal', 'play': 'yes'},
    {'outlook': 'rainy', 'temperature': 'mild', 'humidity': 'high', 'play': 'no'},
    {'outlook': 'sunny', 'temperature': 'cool', 'humidity': 'normal', 'play': 'yes'},
]

# Convertir datos a formato aceptable por FOIL
examples = []
for instance in datos:
    label = instance.pop('play')  # Etiqueta de clasificación
    example = {k: v for k, v in instance.items()}
    examples.append((example, label))

# Definir predicados para FOIL
predicates = [
    Predicate("outlook", ["sunny", "overcast", "rainy"]),
    Predicate("temperature", ["hot", "mild", "cool"]),
    Predicate("humidity", ["high", "normal"])
]

# Crear un objeto FOIL y aprender reglas
foil = Foil(examples, predicates)
rules = foil.learn()

# Imprimir reglas aprendidas
print("Reglas aprendidas por FOIL:")
for rule in rules:
    print(rule)
    