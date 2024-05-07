#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

def negate_literal(literal):
    """
    Negate a literal by adding a '-' in front of it.
    """
    if literal.startswith('-'):
        return literal[1:]
    else:
        return '-' + literal

def skolemize(clause, constants):
    """
    Skolemize existential quantifiers by replacing variables with constants.
    """
    skolemized_clause = clause
    for constant in constants:
        skolemized_clause = skolemized_clause.replace('?', constant)
    return skolemized_clause

def resolve(clause1, clause2):
    """
    Perform resolution between two clauses.
    """
    resolved_clause = []
    for literal in clause1:
        if negate_literal(literal) in clause2:
            resolved_clause.extend([l for l in clause1 if l != literal] + [l for l in clause2 if l != negate_literal(literal)])
    return resolved_clause

def resolution_with_skolem(clauses):
    """
    Perform resolution with Skolemization on a list of clauses.
    """
    constants = ['a', 'b', 'c']  # Constants for Skolemization
    skolemized_clauses = [skolemize(clause, constants) for clause in clauses]

    new_clause = []
    while True:
        new_clause_set = set()
        for i in range(len(skolemized_clauses)):
            for j in range(i + 1, len(skolemized_clauses)):
                new_clause = resolve(skolemized_clauses[i], skolemized_clauses[j])
                if not new_clause:  # Empty clause found, contradiction reached
                    return True
                new_clause_set.add(tuple(new_clause))
        if set(skolemized_clauses).intersection(new_clause_set):  # Check for redundancy
            return False
        skolemized_clauses.extend([list(clause) for clause in new_clause_set])

# Ejemplo de uso
if __name__ == "__main__":
    clauses = [
        ['-P(x)', 'Q(f(x))'],
        ['P(a)'],
        ['-Q(y)'],
        ['P(b)'],
    ]
    result = resolution_with_skolem(clauses)
    if result:
        print("Se encontró una contradicción. La fórmula es válida.")
    else:
        print("No se encontró una contradicción. La fórmula no es válida.")
        