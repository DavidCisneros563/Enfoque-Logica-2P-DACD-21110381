#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from pyDatalog import pyDatalog

# Definir hechos
pyDatalog.create_terms('precedes, iniciado, finalizado')

# Reglas de precedencia
+(precedes[1, 2]) # significa que la acción 1 precede a la acción 2
+(precedes[3, 4])

# Reglas para acciones iniciadas y finalizadas
iniciado(1)
iniciado(3)
finalizado(2)
finalizado(4)

# Reglas para acciones que aún no han finalizado
iniciado(X) <= precedes[X, Y] & finalizado(Y)
finalizado(X) <= iniciado(X) & ~iniciado(Y) & precedes[Y, X]

# Consulta de acciones iniciadas y finalizadas
print("Acciones iniciadas:", iniciado(X))
print("Acciones finalizadas:", finalizado(X))
