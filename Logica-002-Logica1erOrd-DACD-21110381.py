#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from sympy import symbols, ForAll, Exists, And, Or, Not, Implies

# Definir las variables
x, y = symbols('x y')

# Expresiones lógicas
p = x > 0
q = y < 10

# Cuantificación universal y existencial
cuantificacion_universal = ForAll(x, p)
cuantificacion_existencial = Exists(y, q)

# Operaciones lógicas
conjuncion = And(p, q)
disyuncion = Or(p, q)
negacion = Not(p)
implicacion = Implies(p, q)

# Imprimir los resultados
print("Cuantificación universal:", cuantificacion_universal)
print("Cuantificación existencial:", cuantificacion_existencial)
print("Conjunción (p and q):", conjuncion)
print("Disyunción (p or q):", disyuncion)
print("Negación de p:", negacion)
print("Implicación (p implies q):", implicacion)