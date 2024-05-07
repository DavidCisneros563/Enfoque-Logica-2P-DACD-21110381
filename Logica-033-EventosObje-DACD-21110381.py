#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class Creencia:
    def __init__(self, evento, condicion=None):
        self.evento = evento
        self.condicion = condicion

    def evaluar(self):
        if self.condicion:
            return self.condicion()
        else:
            return True

class Agente:
    def __init__(self):
        self.creencias = []

    def agregar_creencia(self, creencia):
        self.creencias.append(creencia)

    def procesar_evento(self, evento):
        for creencia in self.creencias:
            if creencia.evento == evento and creencia.evaluar():
                print(f"El agente cree en el evento: {evento}")

# Funciones de condición para las creencias
def es_lloviendo():
    return True

def es_temporada_verano():
    return False

# Crear instancias de creencias
creencia_lloviendo = Creencia("lluvia", es_lloviendo)
creencia_verano = Creencia("verano", es_temporada_verano)

# Crear instancia de agente
agente = Agente()

# Agregar creencias al agente
agente.agregar_creencia(creencia_lloviendo)
agente.agregar_creencia(creencia_verano)

# Simulación de eventos
agente.procesar_evento("lluvia")
agente.procesar_evento("verano")
