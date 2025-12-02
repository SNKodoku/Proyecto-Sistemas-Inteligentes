import time

class Viewer:

    def __init__(self, environment, decision_maker):
        self.env = environment
        self.dm = decision_maker

    # ------------------------------------------------------
    #  Dibujar mapa estilo ASCII (versión mamalona)
    # ------------------------------------------------------
    def mostrar_mapa(self):
        # posiciones
        ix, iy = self.env.impala.posicion()
        lx, ly = self.env.leon.posicion()

        grid_display = ""

        for fila in range(3):
            for col in range(3):
                if (fila, col) == (ix, iy):
                    grid_display += " [I] "
                elif (fila, col) == (lx, ly):
                    grid_display += " [L] "
                else:
                    grid_display += " [ ] "
            grid_display += "\n"

        print(grid_display)

    # ------------------------------------------------------
    #  Visualizar un paso T
    # ------------------------------------------------------
    def mostrar_paso(self, T, accion_impala, accion_leon):
        print("="*40)
        print(f"Tiempo T = {T}")
        print(f"Impala hizo: {accion_impala}")
        print(f"León hizo:   {accion_leon}")
        print("-"*40)
        print("Mapa:")
        self.mostrar_mapa()
        print("-"*40)
        print("Explicación del león:")
        print(self.dm.explicar())
        print("="*40)

    # ------------------------------------------------------
    #  Cacería paso a paso para el usuario
    # ------------------------------------------------------
    def ejecutar_caceria_paso_a_paso(self):
        print("\n=== Iniciando Cacería Paso a Paso ===\n")

        T = 0
        resultado = "continuar"

        while resultado == "continuar":
            resultado = self.env.step(T)

            # Obtener acciones del historial.
            accion_impala = self.env.historial[-1][1]
            accion_leon = self.env.historial[-1][2]

            self.mostrar_paso(T, accion_impala, accion_leon)

            # Pausar para que el usuario vea el estado
            input("Presiona ENTER para continuar...\n")

            T += 1

        print("\n=== FIN DE LA CACERÍA ===")
        print("Resultado:", resultado.upper())
        print("==========================\n")
