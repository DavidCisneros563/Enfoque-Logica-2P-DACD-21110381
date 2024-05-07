#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class ReglaDecision:
    def __init__(self, condicion, resultado):
        self.condicion = condicion
        self.resultado = resultado

    def evaluar(self, entrada):
        if self.condicion(entrada):
            return self.resultado
        else:
            return None

# Definir algunas reglas de decisión
regla1 = ReglaDecision(lambda x: x > 0, "positivo")
regla2 = ReglaDecision(lambda x: x < 0, "negativo")
regla3 = ReglaDecision(lambda x: x == 0, "cero")

# Función para aplicar las reglas y tomar una decisión
def tomar_decision(reglas, entrada):
    for regla in reglas:
        resultado = regla.evaluar(entrada)
        if resultado:
            return resultado
    return "indefinido"

# Ejemplo de uso
reglas = [regla1, regla2, regla3]
entrada = 5
decision = tomar_decision(reglas, entrada)
print(f"El número {entrada} es {decision}.")