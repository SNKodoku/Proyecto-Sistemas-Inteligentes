import random

class DecisionMaker:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.ultima_explicacion = "Sin explicación aún"
        self.ultima_accion = None

        # conjunto de acciones posibles del león.
        self.acciones_posibles = ["avanzar", "esconderse", "atacar"]

    def decidir(self, situacion):
        """
        Esta función pregunta a la KB si conoce qué hacer.
        Si sí → usa la regla.
        Si no → elige acción aleatoria (exploración).
        """
        accion = self.kb.query(situacion)

        if accion is not None:
            self.ultima_accion = accion
            self.ultima_explicacion = (
                f"Utilicé conocimiento previo: la KB tiene una regla "
                f"que coincide con la situación actual."
            )
            return accion

        # Si no hay regla → el león explora
        accion_random = random.choice(self.acciones_posibles)

        self.ultima_accion = accion_random
        self.ultima_explicacion = (
            "No encontré reglas en la KB, así que tomé "
            f"una acción exploratoria: {accion_random}"
        )

        return accion_random

    def explicar(self):
        """
        Devuelve la explicación de por qué se eligió la acción.
        Útil en modo Cacería Paso a Paso.
        """
        return self.ultima_explicacion
