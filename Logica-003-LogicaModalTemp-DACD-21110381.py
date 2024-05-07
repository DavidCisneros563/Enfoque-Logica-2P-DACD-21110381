#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from fluentpy.temporal import Always, Sometimes
from fluentpy.modal import Possibly, Necessarily
from fluentpy.fuzzy import FuzzyNumber, FuzzySet

# Lógica Temporal
always_true = Always(True)
sometimes_false = Sometimes(False)

# Lógica Modal
possibly_true = Possibly(True)
necessarily_true = Necessarily(True)

# Lógica Difusa
fuzzy_number = FuzzyNumber(5, 2)  # Representa el número 5 con grado de pertenencia 0.2
fuzzy_set = FuzzySet({'bajo': 0.2, 'medio': 0.5, 'alto': 0.8})  # Representa un conjunto difuso con valores de membresía

# Imprimir los resultados
print("Lógica Temporal:")
print("Siempre verdadero:", always_true.evaluate())
print("A veces falso:", sometimes_false.evaluate())

print("\nLógica Modal:")
print("Posiblemente verdadero:", possibly_true.evaluate())
print("Necesariamente verdadero:", necessarily_true.evaluate())

print("\nLógica Difusa:")
print("Número difuso:", fuzzy_number)
print("Conjunto difuso:", fuzzy_set)
