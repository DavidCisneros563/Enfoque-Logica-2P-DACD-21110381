#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import re

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"Token({self.tipo}, '{self.valor}')"

class AnalizadorLexico:
    def __init__(self, texto):
        self.texto = texto
        self.posicion = 0
        self.actual = None
        self.palabras_clave = {'if', 'else', 'while', 'for'}

    def avanzar(self):
        self.posicion += 1
        if self.posicion < len(self.texto):
            self.actual = self.texto[self.posicion]
        else:
            self.actual = None

    def hacer_tokens(self):
        tokens = []
        while self.posicion < len(self.texto):
            if self.actual in [' ', '\n', '\t']:
                self.avanzar()
            elif self.actual.isdigit():
                valor = ''
                while self.actual is not None and self.actual.isdigit():
                    valor += self.actual
                    self.avanzar()
                tokens.append(Token('ENTERO', valor))
            elif self.actual.isalpha() or self.actual == '_':
                valor = ''
                while self.actual is not None and (self.actual.isalnum() or self.actual == '_'):
                    valor += self.actual
                    self.avanzar()
                tipo = 'ID' if valor not in self.palabras_clave else 'PALABRA_CLAVE'
                tokens.append(Token(tipo, valor))
            else:
                tipo = self.actual
                tokens.append(Token(tipo, self.actual))
                self.avanzar()
        return tokens

# Ejemplo de uso
texto = '''
if x == 5:
    y = 10
else:
    y = 20
'''
analizador = AnalizadorLexico(texto)
tokens = analizador.hacer_tokens()
for token in tokens:
    print(token)

    