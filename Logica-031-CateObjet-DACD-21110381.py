#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class Categoria:
    def __init__(self, nombre, padre=None):
        self.nombre = nombre
        self.padre = padre
        self.hijos = []

        if padre:
            padre.agregar_hijo(self)

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def es_ancestro_de(self, categoria):
        if categoria.padre is None:
            return False
        elif categoria.padre == self:
            return True
        else:
            return self.es_ancestro_de(categoria.padre)

# Crear categorías
animal = Categoria("Animal")
mamifero = Categoria("Mamífero", animal)
ave = Categoria("Ave", animal)
perro = Categoria("Perro", mamifero)
gato = Categoria("Gato", mamifero)
loro = Categoria("Loro", ave)

# Verificar relaciones entre categorías
print("¿Animal es ancestro de Perro?", animal.es_ancestro_de(perro))  # True
print("¿Ave es ancestro de Gato?", ave.es_ancestro_de(gato))  # False
print("¿Ave es ancestro de Loro?", ave.es_ancestro_de(loro))  # True
