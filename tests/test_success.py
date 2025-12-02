from environment.grid import Grid
from environment.impala import Impala
from environment.leon import Leon
from environment.environment import Environment
from decision_maker.decision_maker import DecisionMaker
from knowledge.knowledge_base import KnowledgeBase

def test_caceria_exitosa():
    grid = Grid()
    impala = Impala()
    leon = Leon()
    kb = KnowledgeBase()
    dm = DecisionMaker(kb)
    env = Environment(grid, impala, leon, dm)

    # Situación artificial: león justo al lado del impala
    leon.x, leon.y = 1, 0   # oeste del impala
    impala.x, impala.y = 1, 1

    # El león siempre atacará (regla forzada).
    kb.reglas = [{
        "condiciones": {},
        "accion": "atacar"
    }]

    resultado = env.step(0)

    assert resultado == "exito"
