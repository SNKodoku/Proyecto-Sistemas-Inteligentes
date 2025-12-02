import json
from .rule import Rule

class KnowledgeBase:
    def __init__(self):
        self.reglas = []

    # ---------------------------
    #  CONSULTA
    # ---------------------------

    def query(self, situacion):
        """
        Busca la primera regla que coincida.
        """
        for regla in self.reglas:
            if regla.match(situacion):
                return regla.accion
        return None

    # ---------------------------
    #  AGREGAR EXPERIENCIA
    # ---------------------------

    def add_experience(self, situacion, accion, resultado):
        """
        Agrega una nueva regla a la KB sin modificar nada más.
        """
        regla = Rule(condiciones=situacion, accion=accion)
        self.reglas.append(regla)

    # ---------------------------
    #  GENERALIZACIÓN
    # ---------------------------

    def son_similares(self, r1, r2):
        """
        Dos reglas son similares si:
        - Tienen la misma acción
        - Diferencias mínimas entre condiciones
        """
        if r1.accion != r2.accion:
            return False

        diferencias = 0

        for k in r1.condiciones:
            v1 = r1.condiciones[k]
            v2 = r2.condiciones[k]

            # si ambos valores son iguales, no hay pedo
            if v1 == v2:
                continue

            # si difieren más de 1 atributo → NO se pueden generalizar
            diferencias += 1
            if diferencias > 1:
                return False

        return True

    def combinar(self, r1, r2):
        """
        Une las condiciones distintas en un set.
        """
        nuevas_cond = {}

        for k in r1.condiciones:
            v1 = r1.condiciones[k]
            v2 = r2.condiciones[k]

            if v1 == v2:
                nuevas_cond[k] = v1

            else:
                nuevas_cond[k] = {v1, v2}  # generalización

        return Rule(nuevas_cond, r1.accion)

    def generalize(self):
        """
        Busca pares de reglas similares y las combina.
        """
        nueva_lista = []
        skip = set()

        for i in range(len(self.reglas)):
            if i in skip:
                continue

            r1 = self.reglas[i]
            generalizada = r1

            for j in range(i + 1, len(self.reglas)):
                if j in skip:
                    continue

                r2 = self.reglas[j]

                if self.son_similares(generalizada, r2):
                    generalizada = self.combinar(generalizada, r2)
                    skip.add(j)

            nueva_lista.append(generalizada)

        self.reglas = nueva_lista

    # ----------------------------
    #  PERSISTENCIA
    # ----------------------------

    def save(self, filename):
        data = [r.to_dict() for r in self.reglas]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)

        self.reglas = [Rule.from_dict(r) for r in data]
