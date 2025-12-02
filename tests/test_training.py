from environment.grid import Grid
from environment.impala import Impala
from environment.leon import Leon
from environment.environment import Environment
from knowledge.knowledge_base import KnowledgeBase
from decision_maker.decision_maker import DecisionMaker
from training.trainer import Trainer

def test_training_crea_conocimiento():
    grid = Grid()
    impala = Impala()
    leon = Leon()
    kb = KnowledgeBase()
    dm = DecisionMaker(kb)
    env = Environment(grid, impala, leon, dm)

    trainer = Trainer(env, dm, kb)
    trainer.set_posiciones_iniciales([1])  # entrenamiento controlado

    trainer.run(10)  # pequeñas incursiones.

    assert len(kb.reglas) > 0
