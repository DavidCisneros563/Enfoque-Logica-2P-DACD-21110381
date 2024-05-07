#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class Regla:
    def __init__(self, condiciones, conclusion):
        self.condiciones = condiciones
        self.conclusion = conclusion

    def evaluar(self, hechos):
        for condicion in self.condiciones:
            if condicion not in hechos:
                return False
        return True

class MotorDeInferencia:
    def __init__(self, reglas):
        self.reglas = reglas

    def inferir(self, hechos):
        for regla in self.reglas:
            if regla.evaluar(hechos):
                return regla.conclusion
        return None

# Definición de reglas
regla1 = Regla(["fiebre", "tos"], "resfriado")
regla2 = Regla(["fiebre", "dolor_de_cabeza"], "gripe")
regla3 = Regla(["manchas_rojas_en_la_piel"], "sarampión")

# Motor de inferencia con las reglas definidas
motor = MotorDeInferencia([regla1, regla2, regla3])

# Hechos observados
hechos = ["fiebre", "tos"]

# Inferencia
enfermedad = motor.inferir(hechos)

# Resultado
if enfermedad:
    print("El paciente podría tener", enfermedad)
else:
    print("No se pudo determinar la enfermedad.")
    