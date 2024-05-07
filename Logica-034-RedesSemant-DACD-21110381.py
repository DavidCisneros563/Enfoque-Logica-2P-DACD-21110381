#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from pyDatalog import pyDatalog

# Definir reglas
pyDatalog.create_terms('padre, abuelo, tio, X, Y, Z')

+padre('Juan', 'Pedro')
+padre('Pedro', 'Luis')
+padre('Pedro', 'Ana')
+padre('Luis', 'Carlos')

# Regla para calcular abuelo
abuelo(X, Z) <= padre(X, Y) & padre(Y, Z)

# Regla para calcular tio
tio(X, Z) <= padre(Y, Z) & abuelo(X, Y)

# Consultas
print("Abuelos:")
print(abuelo(X, Z))
print("\nTios:")
print(tio(X, Z))
