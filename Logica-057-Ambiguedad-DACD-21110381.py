#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import nltk

# Definir una gramática simple que produzca ambigüedad sintáctica
gramatica_ambigua = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'man' | 'woman' | 'telescope' | 'cat' | 'dog'
    V -> 'saw' | 'ate' | 'walked'
    P -> 'with' | 'in' | 'on'
""")

# Crear un analizador sintáctico basado en la gramática
analizador = nltk.ChartParser(gramatica_ambigua)

# Ejemplo de una oración ambigua
oracion_ambigua = "the man saw the woman with the telescope"

# Tokenizar la oración en palabras individuales
tokens = nltk.word_tokenize(oracion_ambigua)

# Analizar la oración y obtener todos los árboles de análisis sintáctico posibles
arboles = list(analizador.parse(tokens))

# Imprimir todos los árboles sintácticos posibles
print("Árboles sintácticos posibles para la oración ambigua:")
for arbol in arboles:
    print(arbol)
    