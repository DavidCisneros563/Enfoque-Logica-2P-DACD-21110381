#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from sympy import symbols, Not, Or, And, Implies, Equivalent, satisfiable

# Definir símbolos proposicionales
p, q, r = symbols('p q r')

# Definir algunas fórmulas proposicionales
formula_1 = And(p, q)
formula_2 = Or(Not(p), q)
formula_3 = Implies(p, q)
formula_4 = Equivalent(p, q)

# Verificar la equivalencia de dos fórmulas
equivalencia = Equivalent(formula_1, formula_2)
print("¿Las fórmulas 1 y 2 son equivalentes?", equivalencia)

# Verificar la validez de una fórmula
validez = formula_3.is_valid()
print("¿La fórmula 3 es válida?", validez)

# Verificar la satisfacibilidad de una fórmula
satisfacibilidad = satisfiable(formula_4)
print("¿La fórmula 4 es satisfacible?", satisfacibilidad)