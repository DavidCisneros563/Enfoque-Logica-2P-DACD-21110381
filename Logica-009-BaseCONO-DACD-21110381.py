#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

base_conocimiento = {
    "animales": {
        "vertebrados": ["perro", "gato", "elefante"],
        "invertebrados": ["araña", "caracol", "abeja"]
    },
    "colores": {
        "primarios": ["rojo", "azul", "amarillo"],
        "secundarios": ["verde", "naranja", "violeta"]
    },
    "numeros": {
        "pares": [2, 4, 6, 8, 10],
        "impares": [1, 3, 5, 7, 9]
    }
}

def buscar_conocimiento(tema, subtema=None):
    if tema in base_conocimiento:
        if subtema:
            if subtema in base_conocimiento[tema]:
                return base_conocimiento[tema][subtema]
            else:
                return "Subtema no encontrado en la base de conocimiento."
        else:
            return base_conocimiento[tema]
    else:
        return "Tema no encontrado en la base de conocimiento."

# Ejemplo de uso
print(buscar_conocimiento("animales", "vertebrados"))
print(buscar_conocimiento("colores"))
print(buscar_conocimiento("numeros", "pares"))
print(buscar_conocimiento("deportes"))  # Tema no encontrado
print(buscar_conocimiento("animales", "reptiles"))  # Subtema no encontrado