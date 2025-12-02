import pytest
from knowledge.knowledge_base import KnowledgeBase
from knowledge.rule import Rule

def test_kb_generalizacion():
    kb = KnowledgeBase()

    # Dos reglas que deben generalizar
    r1 = Rule(
        {"pos_leon": (0,1), "impala_estado": "izq"},
        "avanzar"
    )
    r2 = Rule(
        {"pos_leon": (0,1), "impala_estado": "der"},
        "avanzar"
    )

    kb.reglas.append(r1)
    kb.reglas.append(r2)

    kb.generalize()

    assert len(kb.reglas) == 1  # se combinan.
    regla = kb.reglas[0]

    assert isinstance(regla.condiciones["impala_estado"], set)
    assert "izq" in regla.condiciones["impala_estado"]
    assert "der" in regla.condiciones["impala_estado"]
