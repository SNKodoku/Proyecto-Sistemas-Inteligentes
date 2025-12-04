import json
from .rule import Rule

class KnowledgeBase:
    def __init__(self):
        self.reglas = []

    # ------------------------------------------------------
    #  CONSULTA
    # ------------------------------------------------------
    def query(self, situacion):
        for regla in self.reglas:
            if regla.match(situacion):
                return regla.accion
        return None

    # ------------------------------------------------------
    #  EXPERIENCIA
    # ------------------------------------------------------
    def add_experience(self, situacion, accion, resultado):
        regla = Rule(condiciones=situacion, accion=accion)
        self.reglas.append(regla)

    # ------------------------------------------------------
    #  SIMILITUD
    # ------------------------------------------------------
    def son_similares(self, r1, r2):
        if r1.accion != r2.accion:
            return False

        diferencias = 0

        for k in r1.condiciones:
            v1 = r1.condiciones[k]
            v2 = r2.condiciones[k]

            if v1 != v2:
                diferencias += 1
                if diferencias > 1:
                    return False

        return True

    # ------------------------------------------------------
    #  COMBINACIÓN
    # ------------------------------------------------------
    def combinar(self, r1, r2):
        nuevas_cond = {}

        for k in r1.condiciones:
            v1 = r1.condiciones[k]
            v2 = r2.condiciones[k]

            if v1 == v2:
                nuevas_cond[k] = v1
                continue

            if isinstance(v1, set) and isinstance(v2, set):
                nuevas_cond[k] = v1.union(v2)

            elif isinstance(v1, set):
                nuevas_cond[k] = v1.union({v2})

            elif isinstance(v2, set):
                nuevas_cond[k] = v2.union({v1})

            else:
                nuevas_cond[k] = {v1, v2}

        return Rule(nuevas_cond, r1.accion)

    # ------------------------------------------------------
    #  GENERALIZACIÓN
    # ------------------------------------------------------
    def generalize(self):
        nueva_lista = []
        skip = set()

        for i in range(len(self.reglas)):
            if i in skip:
                continue

            base = self.reglas[i]

            for j in range(i + 1, len(self.reglas)):
                if j in skip:
                    continue

                if self.son_similares(base, self.reglas[j]):
                    base = self.combinar(base, self.reglas[j])
                    skip.add(j)

            nueva_lista.append(base)

        self.reglas = nueva_lista

    # ------------------------------------------------------
    #  PERSISTENCIA
    # ------------------------------------------------------
    def save(self, filename):
        data = [r.to_dict() for r in self.reglas]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
        self.reglas = [Rule.from_dict(r) for r in data]
