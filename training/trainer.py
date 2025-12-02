import random

class Trainer:
    def __init__(self, environment, decision_maker, knowledge_base):
        self.env = environment
        self.dm = decision_maker
        self.kb = knowledge_base

        # El usuario define las posiciones iniciales permitidas
        self.posiciones_iniciales = [1, 2, 3, 4, 5, 6, 7, 8]

    def set_posiciones_iniciales(self, lista_pos):
        """
        Define desde qué posiciones el león puede iniciar las incursiones.
        Esto lo pide la rúbrica explícitamente.
        """
        self.posiciones_iniciales = lista_pos

    def situar_leon(self, grid, leon):
        """
        Coloca al león en una posición inicial válida seleccionada al azar.
        """
        pos_random = random.choice(self.posiciones_iniciales)
        x, y = grid.posiciones_lion[pos_random]
        leon.x = x
        leon.y = y
        leon.escondido = False
        leon.atacando = False

    def run(self, num_incursiones):
        """
        Ejecuta N incursiones de caza durante el entrenamiento.
        """
        print(f"Entrenando {num_incursiones} incursiones...")

        for i in range(num_incursiones):

            # 1. Reiniciar el entorno para esta incursión
            self.env.impala.__init__()   # reiniciar impala
            self.situar_leon(self.env.grid, self.env.leon)

            T = 0
            resultado = "continuar"

            # 2. Ciclo T de esta incursión
            while resultado == "continuar":
                resultado = self.env.step(T)

                # Obtener la situación que observó el león
                situacion = {
                    "pos_leon": self.env.leon.posicion(),
                    "pos_impala": self.env.impala.posicion(),
                    "distancia": self.env.grid.distancia(self.env.leon, self.env.impala),
                    "en_vision": self.env.grid.en_linea_de_vision(self.env.impala, self.env.leon),
                    "impala_estado": self.env.impala.estado_vision
                }

                # Registrar experiencia real del león
                accion = self.dm.ultima_accion
                self.kb.add_experience(situacion, accion, resultado)

                T += 1

                if T > 200:
                    # failsafe por si algo se atora.
                    resultado = "fracaso"

            # 3. Cuando termina una incursión → generalizar conocimiento
            self.kb.generalize()

            # 4. OUTPUT opcional de seguimiento
            if i % 100 == 0:
                print(f"Progreso: {i}/{num_incursiones}")

        print("Entrenamiento completado.")
