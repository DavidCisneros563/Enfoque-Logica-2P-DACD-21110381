#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

# Representación del conocimiento sobre animales
animales = {
    "perro": {
        "es_mamifero": True,
        "tiene_cuatro_patas": True,
        "hace_guau": True
    },
    "gato": {
        "es_mamifero": True,
        "tiene_cuatro_patas": True,
        "hace_miau": True
    },
    "pajaro": {
        "es_mamifero": False,
        "tiene_cuatro_patas": False,
        "vuela": True
    }
}

# Acceder al conocimiento sobre un animal específico
print("¿El perro es mamífero?", animales["perro"]["es_mamifero"])
print("¿El gato tiene cuatro patas?", animales["gato"]["tiene_cuatro_patas"])
print("¿El pájaro vuela?", animales["pajaro"]["vuela"])