#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir variables de entrada y salida
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir funciones de membresía para las variables
calidad['mala'] = fuzz.trimf(calidad.universe, [0, 0, 5])
calidad['buena'] = fuzz.trimf(calidad.universe, [0, 5, 10])
calidad['excelente'] = fuzz.trimf(calidad.universe, [5, 10, 10])

servicio['pobre'] = fuzz.trimf(servicio.universe, [0, 0, 5])
servicio['aceptable'] = fuzz.trimf(servicio.universe, [0, 5, 10])
servicio['excelente'] = fuzz.trimf(servicio.universe, [5, 10, 10])

propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Visualización de las funciones de membresía
calidad.view()
servicio.view()
propina.view()

# Crear reglas difusas
regla1 = ctrl.Rule(calidad['mala'] | servicio['pobre'], propina['baja'])
regla2 = ctrl.Rule(servicio['aceptable'], propina['media'])
regla3 = ctrl.Rule(servicio['excelente'] | calidad['excelente'], propina['alta'])

# Crear controlador
propina_ctrl = ctrl.ControlSystem([regla1, regla2, regla3])
propina_simulador = ctrl.ControlSystemSimulation(propina_ctrl)

# Simular con valores de entrada
propina_simulador.input['calidad'] = 6.5
propina_simulador.input['servicio'] = 9.8

# Calcular propina
propina_simulador.compute()
print("Valor de propina:", propina_simulador.output['propina'])

# Visualización de la salida
propina.view(sim=propina_simulador)