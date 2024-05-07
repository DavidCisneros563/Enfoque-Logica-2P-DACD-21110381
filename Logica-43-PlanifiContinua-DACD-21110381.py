#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import random

class Tarea:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

class AgenteTrabajador(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.tarea_actual = None

    def step(self):
        if self.tarea_actual is None:
            tarea_disponible = self.model.obtener_tarea_disponible()
            if tarea_disponible:
                self.tarea_actual = tarea_disponible
                print(f"Agente {self.unique_id} comienza a trabajar en {self.tarea_actual.nombre} durante {self.tarea_actual.duracion} pasos.")
                self.model.grilla.place_agent(self, self.model.obtener_ubicacion_disponible())
            else:
                print(f"Agente {self.unique_id} no tiene tareas disponibles.")
        else:
            print(f"Agente {self.unique_id} sigue trabajando en {self.tarea_actual.nombre}.")
            self.tarea_actual.duracion -= 1
            if self.tarea_actual.duracion == 0:
                print(f"Agente {self.unique_id} ha terminado {self.tarea_actual.nombre}.")
                self.tarea_actual = None
                self.model.grilla.remove_agent(self)

class PlanificacionModelo(Model):
    def __init__(self, num_agentes, num_tareas, tamano_grilla):
        self.num_agentes = num_agentes
        self.num_tareas = num_tareas
        self.tamano_grilla = tamano_grilla
        self.grilla = MultiGrid(tamano_grilla, tamano_grilla, True)
        self.programacion = self.generar_programacion()
        self.agenda = self.generar_agenda()

        self.schedule = RandomActivation(self)

        # Crear agentes
        for i in range(self.num_agentes):
            a = AgenteTrabajador(i, self)
            self.schedule.add(a)

        # Colocar agentes en la grilla
        for agent in self.schedule.agents:
            x = random.randrange(self.grilla.width)
            y = random.randrange(self.grilla.height)
            self.grilla.place_agent(agent, (x, y))

    def step(self):
        self.schedule.step()

    def generar_programacion(self):
        programacion = []
        for i in range(self.num_tareas):
            tarea = Tarea(f"Tarea {i+1}", random.randint(1, 5))
            programacion.append(tarea)
        return programacion

    def generar_agenda(self):
        agenda = []
        for tarea in self.programacion:
            agenda.append({"tarea": tarea, "agente": None})
        return agenda

    def obtener_tarea_disponible(self):
        for item in self.agenda:
            if item["agente"] is None:
                return item["tarea"]
        return None

    def obtener_ubicacion_disponible(self):
        x = random.randrange(self.grilla.width)
        y = random.randrange(self.grilla.height)
        return (x, y)

# Configuración del modelo
num_agentes = 3
num_tareas = 5
tamano_grilla = 10

# Crear el modelo
modelo = PlanificacionModelo(num_agentes, num_tareas, tamano_grilla)

# Ejecutar el modelo
for i in range(10):
    print(f"Paso {i+1}:")
    modelo.step()
    print()

print("Ejecución del modelo completa.")
