#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from owlready2 import *

# Crear una ontología
onto = Ontology("http://www.ejemplo.com/ontologia.owl")

# Definir clases en la ontología
class Persona(Thing):
    namespace = onto

class Animal(Thing):
    namespace = onto

class Mamifero(Animal):
    namespace = onto

class Perro(Mamifero):
    namespace = onto

class Gato(Mamifero):
    namespace = onto

# Definir propiedades en la ontología
class tieneMascota(Persona >> Animal):
    namespace = onto

# Crear instancias
juan = Persona("Juan")
pepe = Persona("Pepe")
firulais = Perro("Firulais")
whiskers = Gato("Whiskers")

# Asignar propiedades
juan.tieneMascota.append(firulais)
pepe.tieneMascota.append(whiskers)

# Guardar la ontología en un archivo
onto.save(file="ontologia.owl", format="rdfxml")
