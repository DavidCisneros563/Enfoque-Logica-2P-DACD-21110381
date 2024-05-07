#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from typing import Callable

# Función de aplicación (aplicación de una función a un argumento)
def apply(func: Callable, arg: object) -> object:
    return func(arg)

# Función de abstracción (definición de una función)
def abstract(var: str, body: Callable) -> Callable:
    return lambda x: body(x) if x != var else x

# Función de sustitución (sustitución de una variable por un término)
def substitute(term: Callable, var: str, replacement: Callable) -> Callable:
    return term(replacement) if term == var else term

# Ejemplo de uso
if __name__ == "__main__":
    # Definir una función identidad
    identity = abstract("x", "x")

    # Definir una función que suma 1
    plus_one = abstract("x", apply(lambda x: x + 1, "x"))

    # Aplicar la función identidad a un valor
    result_identity = apply(identity, 5)
    print("Función identidad aplicada a 5:", result_identity)

    # Aplicar la función que suma 1 a un valor
    result_plus_one = apply(plus_one, 5)
    print("Función que suma 1 aplicada a 5:", result_plus_one)

    # Sustituir una variable en una función
    substituted = substitute(abstract("y", "y"), "y", 10)
    print("Sustitución de 'y' por 10:", substituted)

    