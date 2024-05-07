#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from pyswip import Prolog

# Crear un nuevo objeto Prolog
prolog = Prolog()

# Definir hechos y reglas en Prolog
prolog.assertz("padre(juan, pedro)")
prolog.assertz("padre(pedro, maria)")
prolog.assertz("padre(pedro, carlos)")

# Consultar relaciones en Prolog
for solucion in prolog.query("padre(X, Y)"):
    print("X es padre de Y:", solucion["X"], "es padre de", solucion["Y"])

    