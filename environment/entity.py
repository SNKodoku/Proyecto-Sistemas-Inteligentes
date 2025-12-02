# Clase entidad
class Entity:
    def __init__(self, x, y, direccion="NORTE"):
        self.x = x
        self.y = y
        self.direccion = direccion

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def posicion(self):
        return (self.x, self.y)
