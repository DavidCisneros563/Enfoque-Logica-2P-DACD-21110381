#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import nltk
from nltk import induce_pcfg
from nltk.grammar import Nonterminal

# Conjunto de ejemplos para la inducción gramatical
ejemplos = [
    nltk.tree.Tree.fromstring('(S (NP John) (VP saw (NP a man)))'),
    nltk.tree.Tree.fromstring('(S (NP Mary) (VP saw (NP a dog)))'),
    nltk.tree.Tree.fromstring('(S (NP Bob) (VP walked))')
]

# Realizar la inducción gramatical para obtener una gramática probabilística
producciones = []
for arbol in ejemplos:
    producciones.extend(arbol.productions())

# Ajustar una gramática probabilística a partir de los ejemplos
gramatica_probabilistica = induce_pcfg(Nonterminal('S'), producciones)

# Imprimir la gramática inducida
print("Gramática inducida:")
print(gramatica_probabilistica)