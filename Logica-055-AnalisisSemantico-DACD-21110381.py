#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"Token({self.tipo}, '{self.valor}')"

class AnalizadorSemantico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicion = 0
        self.actual = self.tokens[self.posicion]

    def consumir(self, tipo):
        if self.actual.tipo == tipo:
            self.avanzar()
        else:
            raise SyntaxError(f"Error de sintaxis: se esperaba '{tipo}', pero se encontró '{self.actual.tipo}'")

    def avanzar(self):
        self.posicion += 1
        if self.posicion < len(self.tokens):
            self.actual = self.tokens[self.posicion]
        else:
            self.actual = None

    def factor(self):
        token = self.actual
        if token.tipo == 'ENTERO':
            self.consumir('ENTERO')
        elif token.tipo == '(':
            self.consumir('(')
            self.expresion()
            self.consumir(')')
        else:
            raise SyntaxError(f"Error de sintaxis: se esperaba 'ENTERO' o '(', pero se encontró '{token.tipo}'")

    def termino(self):
        self.factor()
        while self.actual is not None and self.actual.tipo in {'*', '/'}:
            operador = self.actual
            self.avanzar()
            self.factor()

    def expresion(self):
        self.termino()
        while self.actual is not None and self.actual.tipo in {'+', '-'}:
            operador = self.actual
            self.avanzar()
            self.termino()

    def analizar(self):
        self.expresion()
        if self.actual is not None:
            raise SyntaxError(f"Error de sintaxis: token inesperado '{self.actual.tipo}'")

    def verificar_semantica(self):
        # Realizar verificaciones semánticas aquí
        pass

# Ejemplo de uso
tokens = [
    Token('ENTERO', '3'),
    Token('+', '+'),
    Token('ENTERO', '4'),
    Token('*', '*'),
    Token('ENTERO', '2')
]
analizador = AnalizadorSemantico(tokens)
analizador.analizar()
analizador.verificar_semantica()
print("Análisis semántico exitoso.")
