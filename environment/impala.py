import random
from .entity import Entity

class Impala(Entity):
    def __init__(self):
        super().__init__(1, 1, direccion="NORTE")
        self.estado_vision = "frente"
        self.modo = "aleatorio"
        self.tiempo_huyendo = 0
        self.huyendo = False

    def actuar(self, T):
        if self.huyendo:
            return "huir"

        acciones = ["ver_izq", "ver_der", "ver_frente", "beber"]
        return random.choice(acciones)

    def huir(self):
        self.huyendo = True
        self.tiempo_huyendo += 1
        velocidad = max(1, self.tiempo_huyendo)

        # huye hacia el ESTE por ejemplo..
        self.mover(0, velocidad)
