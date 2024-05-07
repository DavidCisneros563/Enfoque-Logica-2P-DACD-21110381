#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class Grammar:
    def __init__(self):
        self.terminals = set()
        self.non_terminals = set()
        self.start_symbol = None
        self.productions = {}

    def add_production(self, left_side, right_side):
        if left_side not in self.productions:
            self.productions[left_side] = []
        self.productions[left_side].append(right_side)

        self.non_terminals.add(left_side)
        for symbol in right_side:
            if symbol.isupper():
                self.non_terminals.add(symbol)
            else:
                self.terminals.add(symbol)

    def set_start_symbol(self, symbol):
        self.start_symbol = symbol

    def print_grammar(self):
        print("Terminals:", self.terminals)
        print("Non-terminals:", self.non_terminals)
        print("Start symbol:", self.start_symbol)
        print("Productions:")
        for left_side, right_sides in self.productions.items():
            for right_side in right_sides:
                print(left_side, "->", right_side)

# Ejemplo de uso
grammar = Grammar()

# Definir las producciones de la gramática
grammar.add_production('S', 'aAB')
grammar.add_production('S', 'a')
grammar.add_production('A', 'b')
grammar.add_production('B', 'c')

# Establecer el símbolo inicial
grammar.set_start_symbol('S')

# Imprimir la gramática
print("Gramática:")
grammar.print_grammar()
