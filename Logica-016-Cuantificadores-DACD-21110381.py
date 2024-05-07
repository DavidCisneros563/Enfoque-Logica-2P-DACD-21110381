#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

# Definición del dominio
dominio_personas = ["Juan", "María", "Pedro", "Ana"]

# Predicados
es_hombre = lambda x: x in ["Juan", "Pedro"]
es_mujer = lambda x: x in ["María", "Ana"]
es_padre = lambda x, y: (x == "Juan" and y == "Pedro") or (x == "Pedro" and y == "Juan")
es_madre = lambda x, y: (x == "María" and y == "Ana") or (x == "Ana" and y == "María")

# Cuantificadores
para_todo = lambda P: all(P(x) for x in dominio_personas)
existe = lambda P: any(P(x) for x in dominio_personas)

# Ejemplos de uso
if __name__ == "__main__":
    # Para todo
    print("Para todo hombre, es hombre:", para_todo(es_hombre))  # Debería imprimir True
    print("Para todo hombre, es mujer:", para_todo(es_mujer))    # Debería imprimir False

    # Existe
    print("Existe un hombre que es padre:", existe(lambda x: es_hombre(x) and any(es_padre(x, y) for y in dominio_personas)))  # Debería imprimir True
    print("Existe una mujer que es madre:", existe(lambda x: es_mujer(x) and any(es_madre(x, y) for y in dominio_personas)))    # Debería imprimir True
    