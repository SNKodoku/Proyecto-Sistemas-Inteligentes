# Clase enviroment
class Environment:
    def __init__(self, grid, impala, leon, decision_maker):
        self.grid = grid
        self.impala = impala
        self.leon = leon
        self.dm = decision_maker
        self.historial = []

    def step(self, T):

        # 1. Acción del impala
        accion_impala = self.impala.actuar(T)

        # 2. Construir situación actual
        situacion = {
            "pos_leon": self.leon.posicion(),
            "pos_impala": self.impala.posicion(),
            "distancia": self.grid.distancia(self.leon, self.impala),
            "en_vision": self.grid.en_linea_de_vision(self.impala, self.leon),
            "impala_estado": accion_impala
        }

        # 3. decisión del león
        accion_leon = self.dm.decidir(situacion)

        # 4. Ejecutar acciones
        if accion_impala == "huir":
            self.impala.huir()

        elif accion_impala == "ver_izq":
            self.impala.estado_vision = "izquierda"

        elif accion_impala == "ver_der":
            self.impala.estado_vision = "derecha"

        elif accion_impala == "ver_frente":
            self.impala.estado_vision = "frente"

        elif accion_impala == "beber":
            self.impala.estado_vision = "abajo"

        # Acción del león
        if accion_leon == "avanzar":
            self.leon.avanzar(self.impala)

        elif accion_leon == "esconderse":
            self.leon.esconderse()

        elif accion_leon == "atacar":
            self.leon.atacar(self.impala)

        # 5. Evaluar si debe huir
        if self.grid.en_linea_de_vision(self.impala, self.leon):
            self.impala.huir()

        if situacion["distancia"] < 3:
            self.impala.huir()

        if accion_leon == "atacar":
            self.impala.huir()

        # 6. Registrar
        self.historial.append((T, accion_impala, accion_leon))

        # 7. Resultado final
        if self.impala.posicion() == self.leon.posicion():
            return "exito"

        # si el impala se sale del mapa
        if self.impala.y > 10:
            return "fracaso"

        return "continuar"
