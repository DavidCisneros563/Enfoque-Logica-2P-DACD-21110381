#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import nltk
from nltk import CFG

# Definir la gramática causal
gramatica_causal = CFG.fromstring("""
    S -> NP VP | VP
    NP -> Det N | PropN | NP PP
    VP -> V | V NP | V NP PP
    PP -> P NP
    Det -> 'the'
    N -> 'dog' | 'cat' | 'man' | 'telescope'
    PropN -> 'John' | 'Mary' | 'Bob'
    V -> 'saw' | 'ate' | 'walked'
    P -> 'in' | 'on' | 'by' | 'with'
""")

# Crear un analizador sintáctico basado en la gramática causal
analizador = nltk.ChartParser(gramatica_causal)

# Ejemplo de uso
oracion = "John saw the cat with the telescope"
tokens = nltk.word_tokenize(oracion)
for arbol_sintactico in analizador.parse(tokens):
    print(arbol_sintactico)
    