#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class Accion:
    def __init__(self, nombre, precondiciones=None, efectos=None):
        self.nombre = nombre
        self.precondiciones = precondiciones or []
        self.efectos = efectos or []

    def __str__(self):
        return f"Accion: {self.nombre}"

class Situacion:
    def __init__(self, nombre, estado=None):
        self.nombre = nombre
        self.estado = estado or []

    def __str__(self):
        return f"Situacion: {self.nombre}"

class Evento:
    def __init__(self, nombre, accion, precondiciones=None):
        self.nombre = nombre
        self.accion = accion
        self.precondiciones = precondiciones or []

    def __str__(self):
        return f"Evento: {self.nombre}"

# Crear acciones
comprar = Accion("Comprar", precondiciones=["dinero"], efectos=["producto"])
vender = Accion("Vender", precondiciones=["producto"], efectos=["dinero"])

# Crear situaciones
sin_dinero = Situacion("Sin dinero", estado=["dinero"])
con_dinero = Situacion("Con dinero", estado=["dinero"])

# Crear eventos
evento_compra = Evento("Evento compra", accion=comprar, precondiciones=["Con dinero"])
evento_venta = Evento("Evento venta", accion=vender, precondiciones=["Producto"])

# Mostrar información
print(comprar)
print(vender)
print(sin_dinero)
print(con_dinero)
print(evento_compra)
print(evento_venta)
