#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import time

class Action:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def execute(self):
        print(f"Ejecutando acción: {self.name}")
        time.sleep(self.duration)
        print(f"¡Acción {self.name} completada!")

class ExecutionMonitor:
    def __init__(self, actions):
        self.actions = actions
        self.execution_queue = actions.copy()

    def monitor_execution(self):
        while self.execution_queue:
            current_action = self.execution_queue[0]
            print(f"Iniciando ejecución de la acción: {current_action.name}")
            current_action.execute()
            self.execution_queue.pop(0)
            print(f"Acción {current_action.name} completada.")

            if self.execution_queue:
                next_action = self.execution_queue[0]
                print(f"Siguiente acción: {next_action.name}")

    def replanificar(self, action_index):
        print(f"Replanificando después de la acción {action_index}")
        self.execution_queue = self.actions[action_index:]

# Definir acciones
acciones = [
    Action("Paso 1", 2),
    Action("Paso 2", 3),
    Action("Paso 3", 4),
    Action("Paso 4", 2),
]

# Crear monitor de ejecución
monitor = ExecutionMonitor(acciones)

# Iniciar monitoreo de ejecución
monitor.monitor_execution()

# Simular una situación de falla y replanificar
indice_accion_fallida = 2
monitor.replanificar(indice_accion_fallida)

# Volver a monitorear la ejecución
monitor.monitor_execution()