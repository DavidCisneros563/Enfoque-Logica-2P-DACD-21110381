#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class Tarea:
    def __init__(self, nombre, sub_tareas=None):
        self.nombre = nombre
        self.sub_tareas = sub_tareas or []

    def agregar_sub_tarea(self, sub_tarea):
        self.sub_tareas.append(sub_tarea)

    def __str__(self):
        return self.nombre

def ejecutar_tarea(tarea):
    print("Ejecutando tarea:", tarea)
    for sub_tarea in tarea.sub_tareas:
        ejecutar_tarea(sub_tarea)

# Crear tareas
tarea_principal = Tarea("Tarea Principal")
sub_tarea1 = Tarea("Subtarea 1")
sub_tarea2 = Tarea("Subtarea 2")
sub_tarea3 = Tarea("Subtarea 3")
sub_sub_tarea1 = Tarea("Subsubtarea 1")

# Construir la jerarquía de tareas
tarea_principal.agregar_sub_tarea(sub_tarea1)
tarea_principal.agregar_sub_tarea(sub_tarea2)
tarea_principal.agregar_sub_tarea(sub_tarea3)
sub_tarea1.agregar_sub_tarea(sub_sub_tarea1)

# Ejecutar tarea principal
ejecutar_tarea(tarea_principal)