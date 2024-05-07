#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import itertools

def tabla_verdad(expresion):
    variables = sorted(set([char for char in expresion if char.isalpha()]))
    valores_posibles = list(itertools.product([False, True], repeat=len(variables)))

    print("Variables:", variables)
    print("Tabla de Verdad:")

    for valores in valores_posibles:
        asignaciones = dict(zip(variables, valores))
        resultado = eval(expresion, asignaciones)
        print([asignaciones[var] for var in variables], ":", resultado)

# Ejemplo de uso
expresion = "A and (B or C)"
tabla_verdad(expresion)