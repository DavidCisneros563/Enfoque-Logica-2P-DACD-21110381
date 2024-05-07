#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import random

class AgenteRacional:
    def __init__(self, creencias, acciones, utilidades):
        self.creencias = creencias  # Distribución de creencias sobre el estado del mundo
        self.acciones = acciones  # Conjunto de posibles acciones que el agente puede tomar
        self.utilidades = utilidades  # Función de utilidad que asigna una utilidad a cada acción

    def tomar_decision(self):
        mejor_accion = None
        mejor_utilidad = float('-inf')

        # Calcular la utilidad esperada de cada acción y elegir la mejor
        for accion in self.acciones:
            utilidad_esperada = sum(self.utilidades[accion][estado] * probabilidad
                                    for estado, probabilidad in self.creencias.items())
            if utilidad_esperada > mejor_utilidad:
                mejor_utilidad = utilidad_esperada
                mejor_accion = accion

        return mejor_accion

# Ejemplo de uso
creencias = {'estado1': 0.3, 'estado2': 0.7}  # Ejemplo de distribución de creencias
acciones = ['accion1', 'accion2']  # Ejemplo de acciones posibles
utilidades = {'accion1': {'estado1': 0.8, 'estado2': 0.2},  # Ejemplo de función de utilidad
              'accion2': {'estado1': 0.2, 'estado2': 0.8}}

# Crear un agente racional con las creencias, acciones y utilidades definidas
agente = AgenteRacional(creencias, acciones, utilidades)

# Tomar una decisión
accion_elegida = agente.tomar_decision()
print("El agente elige la acción:", accion_elegida)
