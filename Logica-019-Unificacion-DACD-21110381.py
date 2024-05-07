#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

def unify(x, y, theta):
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x.islower():
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.islower():
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None
        else:
            for xi, yi in zip(x, y):
                theta = unify(xi, yi, theta)
            return theta
    else:
        return None

# Ejemplo de uso
theta = {}
x = ['P', 'x', 'y']
y = ['P', 'A', 'B']
print("Unificación:", unify(x, y, theta))
