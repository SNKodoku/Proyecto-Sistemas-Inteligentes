from environment.grid import Grid
from environment.impala import Impala
from environment.leon import Leon
from environment.environment import Environment

from knowledge.knowledge_base import KnowledgeBase
from decision_maker.decision_maker import DecisionMaker

from training.trainer import Trainer
from ui.viewer import Viewer


def main():

    print("\n=======================================")
    print(" SISTEMA INTELIGENTE: LEÓN VS IMPALA")
    print(" Proyecto Final - Sistemas Inteligentes")
    print("=======================================\n")

    # ------------------------------------------
    # 1. Crear mundo, animales y cerebro.
    # ------------------------------------------
    grid = Grid()
    impala = Impala()
    leon = Leon()

    kb = KnowledgeBase()
    dm = DecisionMaker(kb)

    env = Environment(grid, impala, leon, dm)

    # -----------------------------------------
    # 2. Entrenamiento
    # -----------------------------------------
    print("CONFIGURANDO ENTRENAMIENTO...\n")

    trainer = Trainer(env, dm, kb)

    # Definir posiciones iniciales válidas
    # Ejemplo clásico de la rúbrica:
    # Entrenar solo desde la posición 3
    # trainer.set_posiciones_iniciales([3])

    # Entrenar desde todas las posiciones menos 5
    trainer.set_posiciones_iniciales([1,2,3,4,6,7,8])

    num_incursiones = 5000  # cámbiale dependiendo qué tan pro quieras el aprendizaje

    print(f"Iniciando entrenamiento con {num_incursiones} incursiones...\n")
    print(dir(kb))
    trainer.run(num_incursiones)

    # Guardar conocimiento
    kb.save("conocimiento.json")
    print("\nConocimiento guardado en 'conocimiento.json'")

    # -----------------------------------------
    # 3. Modo cacería paso a paso
    # -----------------------------------------
    print("\n=======================================")
    print("     MODO CACERÍA PASO A PASO")
    print("=======================================\n")

    viewer = Viewer(env, dm)

    # Reiniciar animales para una cacería limpia
    impala.__init__()
    leon.__init__()

    # Situar el león donde tú quieras para la demo
    x, y = grid.posiciones_lion[3]  # ejemplo posición 3
    leon.x = x
    leon.y = y

    # Ejecutar cacería lenta
    viewer.ejecutar_caceria_paso_a_paso()

    print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()
