from environment.grid import Grid
from environment.impala import Impala
from environment.leon import Leon
from environment.environment import Environment
from decision_maker.decision_maker import DecisionMaker
from knowledge.knowledge_base import KnowledgeBase

def test_caceria_fallida():
    grid = Grid()
    impala = Impala()
    leon = Leon()
    kb = KnowledgeBase()
    dm = DecisionMaker(kb)
    env = Environment(grid, impala, leon, dm)

    # Forzar que el impala huya inmediatamente.
    impala.huyendo = True
    impala.x, impala.y = 1, 1

    resultado = env.step(0)

    assert resultado == "fracaso"
