import math

class Grid:
    def __init__(self):
        # Mapa simple 3x3 como el del PDF.
        # Coordenadas:
        # (fila, columna) 0 arriba
        self.mapa = [
            [8, 1, 2],
            [7, "I", 3],
            [6, 5, 4]
        ]

        # posiciones válidas del león
        self.posiciones_lion = {
            1: (0, 1),
            2: (0, 2),
            3: (1, 2),
            4: (2, 2),
            5: (2, 1),
            6: (2, 0),
            7: (1, 0),
            8: (0, 0)
        }

        self.impala_pos = (1, 1)  # siempre fija en el centro

    def distancia(self, a, b):
        return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

    def en_linea_de_vision(self, impala, leon):
        # visión simplificada: impala mira hacia el norte,
        # y ve cuadro frente, frente-izq y frente-der (según PDF)
        ix, iy = impala.posicion()
        lx, ly = leon.posicion()

        # visión frontal
        if lx == ix - 1 and ly == iy:
            return not leon.escondido

        # visión diagonal izquierda
        if lx == ix - 1 and ly == iy - 1:
            return not leon.escondido

        # visión diagonal derecha
        if lx == ix - 1 and ly == iy + 1:
            return not leon.escondido

        return False
