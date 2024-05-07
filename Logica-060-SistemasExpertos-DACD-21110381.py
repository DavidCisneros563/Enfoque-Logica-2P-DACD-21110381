#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class MotorInferencia:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def inferir(self, objetivo):
        while True:
            reglas_activadas = [regla for regla in self.base_conocimiento if regla.si_cumple()]
            if not reglas_activadas:
                break
            for regla in reglas_activadas:
                regla.aplicar_consecuencia()
                if regla.consecuencia == objetivo:
                    return True
        return False

class Regla:
    def __init__(self, antecedentes, consecuencia):
        self.antecedentes = antecedentes
        self.consecuencia = consecuencia

    def si_cumple(self):
        # Aquí iría la lógica para verificar si los antecedentes de la regla se cumplen
        return True  # Devuelve True si se cumplen, False en caso contrario

    def aplicar_consecuencia(self):
        # Aquí iría la lógica para aplicar la consecuencia de la regla
        pass

# Ejemplo de uso
if __name__ == "__main__":
    # Definir la base de conocimiento (reglas)
    reglas = [
        Regla(["temperatura_alta", "presion_alta"], "riesgo_alto"),
        Regla(["temperatura_baja", "presion_baja"], "riesgo_bajo")
        # Agrega más reglas según el dominio del problema
    ]

    # Crear el motor de inferencia con la base de conocimiento
    motor = MotorInferencia(reglas)

    # Realizar una inferencia
    objetivo = "riesgo_alto"
    resultado = motor.inferir(objetivo)

    # Imprimir el resultado de la inferencia
    if resultado:
        print(f"Se encontró evidencia de '{objetivo}'.")
    else:
        print(f"No se encontró evidencia de '{objetivo}'.")
        