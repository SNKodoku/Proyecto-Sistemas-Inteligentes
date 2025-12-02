class Rule:
    """
    Una regla es de la forma:
    condiciones = {
        "pos_leon": (x,y),
        "pos_impala": (x,y),
        "distancia": valor,
        "en_vision": True/False,
        "impala_estado": "ver_frente"
    }

    accion = "avanzar", "esconderse" o "atacar"
    """

    def __init__(self, condiciones, accion, confianza=1):
        self.condiciones = condiciones
        self.accion = accion
        self.confianza = confianza  # útil si quieres RL sencillo.

    def match(self, situacion):
        """
        Compara cada atributo de la situación con las condiciones.
        Si la condición es un SET, permite coincidencias múltiples (generalización).
        """
        for clave, valor_cond in self.condiciones.items():
            valor_sit = situacion.get(clave)

            # caso normal
            if isinstance(valor_cond, set):
                if valor_sit not in valor_cond:
                    return False

            # caso exacto
            else:
                if valor_sit != valor_cond:
                    return False

        return True

    def to_dict(self):
        # convierte sets en listas para JSON
        condiciones_json = {
            k: list(v) if isinstance(v, set) else v
            for k, v in self.condiciones.items()
        }
        return {
            "condiciones": condiciones_json,
            "accion": self.accion,
            "confianza": self.confianza
        }

    @staticmethod
    def from_dict(data):
        condiciones = {
            k: set(v) if isinstance(v, list) else v
            for k, v in data["condiciones"].items()
        }

        return Rule(
            condiciones=condiciones,
            accion=data["accion"],
            confianza=data.get("confianza", 1)
        )
