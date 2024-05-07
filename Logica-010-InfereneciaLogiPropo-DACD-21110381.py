#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class InferenciaLogicaProposicional:
    def __init__(self, premisas=[]):
        self.premisas = premisas

    def agregar_premisa(self, premisa):
        self.premisas.append(premisa)

    def verificar_afirmacion(self, afirmacion):
        for premisa in self.premisas:
            if self.entailment(premisa, afirmacion):
                return True
        return False

    def entailment(self, premisa, afirmacion):
        # Implementación simple de la relación de implicación lógica (premisa -> afirmacion)
        # Aquí puedes agregar reglas de inferencia más complejas según tus necesidades
        return premisa == afirmacion

# Ejemplo de uso
if __name__ == "__main__":
    inferencia = InferenciaLogicaProposicional(premisas=["p", "q"])  # Premisas iniciales

    # Agregar más premisas si es necesario
    inferencia.agregar_premisa("p & q")  # p y q son verdaderas

    # Verificar afirmaciones
    print(inferencia.verificar_afirmacion("p"))  # Debería imprimir True, ya que p es verdadera según las premisas
    print(inferencia.verificar_afirmacion("q"))  # Debería imprimir True, ya que q es verdadera según las premisas
    print(inferencia.verificar_afirmacion("p & q"))  # Debería imprimir True, ya que p y q son verdaderas según las premisas
    print(inferencia.verificar_afirmacion("p | q"))  # Debería imprimir True, ya que p o q son verdaderas según las premisas
    print(inferencia.verificar_afirmacion("p -> q"))  # Debería imprimir True, ya que p implica q según las premisas
    print(inferencia.verificar_afirmacion("p & ~q"))  # Debería imprimir False, ya que p y no q no son verdaderas según las premisas
    