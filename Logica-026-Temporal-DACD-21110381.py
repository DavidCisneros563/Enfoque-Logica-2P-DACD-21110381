#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from pytemporal import *

# Crear fórmulas de lógica temporal
formula1 = Atom("p")
formula2 = Atom("q")
formula3 = Negation(Next(Atom("p")))
formula4 = Conjunction(Atom("p"), Atom("q"))
formula5 = Until(Atom("p"), Atom("q"))

# Evaluar fórmulas en un modelo temporal
model = KripkeStructure()
model.add_states("s1", "s2", "s3")
model.add_transition("s1", "s2")
model.add_transition("s2", "s3")
model.add_label("s1", "p")
model.add_label("s2", "q")
model.add_label("s3", "p")

# Verificar satisfacción de fórmulas en el modelo
print("¿La fórmula p es válida en el modelo? ", model.satisfies("s1", formula1))
print("¿La fórmula q es válida en el modelo? ", model.satisfies("s1", formula2))
print("¿La fórmula ¬Xp es válida en el modelo? ", model.satisfies("s1", formula3))
print("¿La fórmula p ∧ q es válida en el modelo? ", model.satisfies("s1", formula4))
print("¿La fórmula p U q es válida en el modelo? ", model.satisfies("s1", formula5))
