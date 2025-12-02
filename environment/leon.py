from .entity import Entity

class Leon(Entity):
    def __init__(self):
        # Se inicia en una posición al azar, pero el Trainer la controla
        super().__init__(0, 0)
        self.escondido = False
        self.atacando = False
        self.ultima_accion = None

    def avanzar(self, impala):
        ix, iy = impala.posicion()
        lx, ly = self.posicion()

        dx = 0
        dy = 0

        if ix < lx:
            dx = -1
        elif ix > lx:
            dx = 1

        if iy < ly:
            dy = -1
        elif iy > ly:
            dy = 1

        self.mover(dx, dy)
        self.escondido = False
        self.atacando = False
        self.ultima_accion = "avanzar"

    def esconderse(self):
        self.escondido = True
        self.ultima_accion = "esconderse"

    def atacar(self, impala):
        # avanza 2 cuadros hacia el impala..
        ix, iy = impala.posicion()
        lx, ly = self.posicion()

        dx = 0 if ix == lx else (1 if ix > lx else -1)
        dy = 0 if iy == ly else (1 if iy > ly else -1)

        self.mover(dx * 2, dy * 2)
        self.atacando = True
        self.ultima_accion = "atacar"
