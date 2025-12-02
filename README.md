Proyecto Final – Sistemas Inteligentes 2026-I

Simulación de un león aprendiendo a cazar un impala mediante aprendizaje basado en experiencia.

---------------------Descripción General---------------------

Este proyecto implementa un sistema inteligente que permite que un león aprenda por sí mismo cómo cazar un impala bajo diferentes condiciones, tal como lo solicita la rúbrica oficial del curso de Sistemas Inteligentes.

El sistema simula:

 -El comportamiento del impala (visión, beber agua, huir).

 -El comportamiento del león (avanzar, esconderse, atacar).

 -La interacción ciclo a ciclo (unidad de tiempo T).

 -Una fase de entrenamiento con miles de incursiones.

 -Una base de conocimiento dinámica que generaliza reglas.

 -Una cacería paso a paso con explicaciones, donde el usuario puede preguntar “¿por qué hizo eso el león?”.

 Objetivo del Sistema

Que el león:

 -Aprenda mediante experiencia (no se le programa explícitamente qué hacer).

 -Descubra estrategias óptimas basándose en reglas observadas.

 -Generalice su conocimiento cuando existen patrones repetidos.

 -Tome decisiones inteligentes basadas en una Knowledge Base (KB).

---------------------Arquitectura del Proyecto---------------------

proyecto_SI/
│── environment/          # Mundo virtual (grid, león, impala)
│   ├── grid.py
│   ├── entity.py
│   ├── impala.py
│   ├── leon.py
│   └── environment.py
│
│── knowledge/            # Sistema experto (reglas + generalización)
│   ├── rule.py
│   └── knowledge_base.py
│
│── decision_maker/       # Motor de decisiones del león
│   └── decision_maker.py
│
│── training/             # Entrenamiento automático
│   └── trainer.py
│
│── ui/                   # Cacería paso a paso
│   └── viewer.py
│
│── tests/                # Pruebas unitarias
│   ├── test_success.py
│   ├── test_fail.py
│   ├── test_kb.py
│   └── test_training.py
│
│── data/
│   └── conocimiento.json # Base de conocimiento guardada
│
└── main.py               # Punto de entrada del proyecto

---------------------Instalación---------------------

1. Clonar el repositorio.

git clone https://github.com/usuario/proyecto_SI.git
cd proyecto_SI

2. Instalar dependencias.
El proyecto usa pytest para pruebas.

py -m pip install pytest

---------------------Ejecución del Sistema---------------------

Entrenar al león

Edita main.py si quieres cambiar el número de incursiones o posiciones iniciales.
Luego ejecuta:

py main.py

Durante el entrenamiento se generará automáticamente el archivo:

data/conocimiento.json

---------------------Modo: Cacería Paso a Paso---------------------

Al terminar el entrenamiento, el sistema entra al modo de simulación:

Se muestra el mapa ciclo por ciclo.

Se muestran las acciones del impala y del león.

Se puede ver la explicación del motor de decisiones.

El usuario avanza la simulación con ENTER.

Ejemplo del mapa ASCII:

T = 3
Impala: ver_frente
León: avanzar

Mapa:
 [ ] [L] [ ]
 [ ] [ I ] [ ]
 [ ] [ ] [ ]

---------------------Base de Conocimiento (Knowledge Base)---------------------

El león aprende reglas de la forma:

(Situación) -> (Acción óptima)

Ejemplo:

{pos_leon=(0,1), impala_estado='izq'} ---> avanzar
{pos_leon=(0,1), impala_estado='der'} ---> avanzar

El sistema generaliza automáticamente:

{pos_leon=(0,1), impala_estado={'izq','der'}} ---> avanzar

---------------------Pruebas Unitarias---------------------

Ejecuta todas las pruebas con:

pytest tests/

Las pruebas cubren:

 -Cacería exitosa

 -Cacería fallida

 -Manejo de la KB

 -Proceso de entrenamiento

 --------------------- Diagramas ---------------------

1. DIAGRAMA GENERAL DE ARQUITECTURA (Vista de módulos)
                ┌───────────────────────────┐
                │        UI / Viewer        │
                │  - Cacería paso a paso    │
                │  - Explicaciones "por qué"│
                └───────────────┬───────────┘
                                │
                                ▼
            ┌────────────────────────────────────────┐
            │              DECISION MAKER             │
            │     - Consulta KB                      │
            │     - Selecciona acción del león       │
            └──────────────────────┬─────────────────┘
                                   │
                                   ▼
            ┌────────────────────────────────────────┐
            │             KNOWLEDGE BASE              │
            │  - Reglas                              │
            │  - Generalización automática            │
            │  - Guardar / cargar                    │
            └──────────────────────┬─────────────────┘
                                   │
                                   ▼
    ┌─────────────────────────────────────────────────────────┐
    │                        TRAINER                           │
    │   - Corre miles de incursiones                           │
    │   - Registra experiencia                                 │
    │   - Actualiza KB                                         │
    └──────────────────────┬───────────────────────────────────┘
                           │
                           ▼
    ┌─────────────────────────────────────────────────────────┐
    │                      ENVIRONMENT                         │
    │   - Grid                                                 │
    │   - Impala                                               │
    │   - León                                                 │
    │   - Reglas del mundo y visión                            │
    │   - Detección de huida / fin                             │
    └─────────────────────────────────────────────────────────┘

2. UML DE CLASES (versión clara + profesional)
┌─────────────────────┐
│      Entity         │
│─────────────────────│
│ + x:int             │
│ + y:int             │
│ + direccion         │
│─────────────────────│
│ + mover()           │
└───────┬─────────────┘
        │
 ┌──────┴─────────┐                ┌─────────────────────────┐
 │    Impala      │                │         Leon            │
 │────────────────│                │─────────────────────────│
 │ +estado_vision │                │ +escondido:bool         │
 │────────────────│                │─────────────────────────│
 │ +ver_izq()     │                │ +avanzar()              │
 │ +ver_der()     │                │ +esconderse()           │
 │ +ver_frente()  │                │ +atacar()               │
 │ +beber()       │                │ +situar_en_pos(int)     │
 │ +huir()        │                └─────────────────────────┘
 └────────────────┘

┌──────────────────────────────┐
│            Grid               │
│──────────────────────────────│
│ +mapa[][]                     │
│ +posiciones_validas           │
│──────────────────────────────│
│ +linea_vision(impala, leon)   │
│ +distancia(a, b)              │
└──────────────────────────────┘

┌────────────────────────────────────┐
│            Environment             │
│────────────────────────────────────│
│ +grid                              │
│ +impala                            │
│ +leon                              │
│ +historial                         │
│────────────────────────────────────│
│ +step()                            │
│ +evaluar_huida()                   │
│ +fin_caceria()                     │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│          DecisionMaker             │
│────────────────────────────────────│
│ +kb: KnowledgeBase                 │
│────────────────────────────────────│
│ +decidir(situacion)               │
│ +explicar()                       │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│           KnowledgeBase            │
│────────────────────────────────────│
│ +reglas: list<Rule>                │
│────────────────────────────────────│
│ +query(situacion)                 │
│ +add_experience()                 │
│ +generalize()                     │
│ +save()                           │
│ +load()                           │
└────────────────────────────────────┘

┌──────────────────────────┐
│          Rule            │
│──────────────────────────│
│ +condiciones             │
│ +accion                  │
│ +confianza               │
│──────────────────────────│
│ +match(situacion)        │
└──────────────────────────┘

┌───────────────────────────┐
│         Trainer           │
│───────────────────────────│
│ +n_incursiones           │
│ +pos_iniciales           │
│───────────────────────────│
│ +run()                   │
│ +registrar_experiencia() │
└───────────────────────────┘

3. DIAGRAMA DE SECUENCIA (Ciclo T, paso a paso)
 Usuario          Viewer        Environment       Impala          DecisionMaker      Leon       KB
    |                |              |               |                   |              |         |
    |---- start ---->|              |               |                   |              |         |
    |                |---- step --->|               |                   |              |         |
    |                |              |---- act ------> Impala hace acción según modo    |         |
    |                |              |               |                                  |         |
    |                |              |---- solicitar_situación ------------------------>|         |
    |                |              |                                            |---- query --->|
    |                |              |                                           |<--- acción ----|
    |                |              |<--- acción_decidida -----------------------|               |
    |                |              |--------------- ejecutar_accion_leon ---------------------->|
    |                |              |--------------- evaluar_huida() --------------------------->|
    |                |              |--------------- actualizar_estado() ----------------------->|
    |                |<------------- devolver_resultado -----------------------------------------|
    |<---- mostrar---|              |               |                   |              |         |

---------------------Diagramas en formato ASCII---------------------

1. ARQUITECTURA GENERAL DEL SISTEMA (ASCII)
                   ┌─────────────────────────────┐
                   │           UI / Viewer        │
                   │  - Visualización paso a paso │
                   │  - "¿Por qué?" del león      │
                   └───────────────┬─────────────┘
                                   │
                                   ▼
                   ┌──────────────────────────────────┐
                   │         Decision Maker            │
                   │  - Consulta la KB                 │
                   │  - Selecciona acción del león     │
                   └──────────────────┬────────────────┘
                                      │
                                      ▼
         ┌──────────────────────────────────────────────────────────┐
         │                      Knowledge Base                      │
         │   - Reglas                                              │
         │   - Generalización automática                           │
         │   - Guardar / cargar reglas                             │
         └─────────────────────┬────────────────────────────────────┘
                               │
                               ▼
         ┌──────────────────────────────────────────────────────────┐
         │                         Trainer                          │
         │   - Corre miles de incursiones                           │
         │   - Registra experiencias                                │
         │   - Actualiza KB                                         │
         └─────────────────────┬────────────────────────────────────┘
                               │
                               ▼
         ┌──────────────────────────────────────────────────────────┐
         │                       Environment                        │
         │   - Grid                                                 │
         │   - León                                                 │
         │   - Impala                                               │
         │   - Lógica de visión / huida                             │
         │   - Termina en éxito o fracaso                           │
         └──────────────────────────────────────────────────────────┘

2. UML DE CLASES (ASCII)
                         ┌───────────────┐
                         │    Entity     │
                         ├───────────────┤
                         │ +x:int        │
                         │ +y:int        │
                         │ +direccion    │
                         ├───────────────┤
                         │ +mover()      │
                         └───────┬───────┘
                                 │
        ┌────────────────────────┴────────────────────────┐
        │                                                 │
┌───────────────┐                               ┌────────────────┐
│    Impala     │                               │      Leon      │
├───────────────┤                               ├────────────────┤
│ +estado_vision│                               │ +escondido     │
├───────────────┤                               ├────────────────┤
│ +ver_izq()    │                               │ +avanzar()     │
│ +ver_der()    │                               │ +esconderse()  │
│ +ver_frente() │                               │ +atacar()      │
│ +beber()      │                               │ +situar(pos)   │
│ +huir()       │                               └────────────────┘
└───────────────┘

┌──────────────────────────────┐
│            Grid               │
├──────────────────────────────┤
│ +mapa[][]                    │
│ +posiciones_validas          │
├──────────────────────────────┤
│ +linea_vision()              │
│ +distancia()                 │
└──────────────────────────────┘

┌──────────────────────────────────────┐
│              Environment             │
├──────────────────────────────────────┤
│ +grid                                │
│ +impala                              │
│ +leon                                │
│ +historial                           │
├──────────────────────────────────────┤
│ +step()                              │
│ +evaluar_huida()                     │
│ +fin_caceria()                       │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│            DecisionMaker             │
├──────────────────────────────────────┤
│ +kb:KnowledgeBase                    │
├──────────────────────────────────────┤
│ +decidir(sit)                        │
│ +explicar()                          │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│            KnowledgeBase             │
├──────────────────────────────────────┤
│ +reglas: list<Rule>                  │
├──────────────────────────────────────┤
│ +query()                             │
│ +add_experience()                    │
│ +generalize()                        │
│ +save()                              │
│ +load()                              │
└──────────────────────────────────────┘

┌──────────────────────────┐
│          Rule            │
├──────────────────────────┤
│ +condiciones             │
│ +accion                  │
│ +confianza               │
├──────────────────────────┤
│ +match()                 │
└──────────────────────────┘

┌──────────────────────────┐
│         Trainer          │
├──────────────────────────┤
│ +n_incursiones           │
│ +pos_iniciales           │
├──────────────────────────┤
│ +run()                   │
│ +registrar_experiencia() │
└──────────────────────────┘

3. DIAGRAMA DE SECUENCIA DEL CICLO T (ASCII)
Usuario         Viewer         Environment        Impala       DecisionMaker      Leon          KB
   |              |                |                |               |               |            |
   |---- start --->                |                |               |               |            |
   |              |---- step ----->|                |               |               |            |
   |              |                |---- acción ----> Impala actúa  |               |            |
   |              |                |                |               |               |            |
   |              |                |---- obtener_situación -------->|               |            |
   |              |                |                                |---- query --->|------------>|
   |              |                |                                |<-- acción ----|<------------|
   |              |                |<--- acción_decidida -----------|               |            |
   |              |                |---- ejecutar_accion_leon --------------------->|            |
   |              |                |---- evaluar_huida() -------------------------->|            |
   |              |                |---- actualizar_estado() ---------------------->|            |
   |              |<--------------- devolver_resultado ------------------------------|            |
   |<---- mostrar estado ----------|                |               |               |            |

4. DIAGRAMA DEL FLUJO DE ENTRENAMIENTO (ASCII)
                   ┌────────────────────────┐
                   │    Iniciar ciclo N     │
                   └───────────┬────────────┘
                               ▼
                 ┌────────────────────────────┐
                 │ Seleccionar posición inicial│
                 └───────────┬────────────────┘
                             ▼
                 ┌────────────────────────────┐
                 │    Crear nueva cacería     │
                 └───────────┬────────────────┘
                             ▼
           ┌──────────────────────────────────────────┐
           │    Repetir mientras no termine la caza   │
           └──────────────────────────────────────────┘
                             │
       ┌─────────────────────┼────────────────────────┐
       ▼                     ▼                        ▼
┌───────────────┐    ┌──────────────────┐     ┌─────────────────────┐
│ Impala actúa  │    │ León decide acción│     │ Environment evalúa  │
└───────────────┘    └──────────────────┘     └─────────────────────┘
                             │
                             ▼
                ┌──────────────────────────────┐
                │ Registrar experiencia en KB  │
                └──────────────────────────────┘
                             │
                             ▼
                   ┌────────────────────────┐
                   │ Fin de la incursión    │
                   └───────────┬------------┘
                               ▼
                    ┌─────────────────────────┐
                    │ KB.generalize()         │
                    └───────────┬────────────┘
                                ▼
                      ┌────────────────────┐
                      │ Siguiente incursión│
                      └────────────────────┘

5. DIAGRAMA DEL PROCESO DE GENERALIZACIÓN (ASCII)
          ┌──────────────────────────────────────────────┐
          │  Reglas originales en KB                     │
          │  Ej:                                          │
          │   (pos=1, impala=izq) → avanzar               │
          │   (pos=1, impala=der) → avanzar               │
          └───────────────────────┬──────────────────────┘
                                  ▼
                     ┌────────────────────────┐
                     │ Detectar similitudes   │
                     │ - misma acción          │
                     │ - condiciones similares │
                     └───────────┬────────────┘
                                 ▼
                   ┌──────────────────────────────┐
                   │ Crear regla generalizada      │
                   │ Ej:                           │
                   │  (pos=1, impala={izq,der}) → avanzar
                   └───────────┬──────────────────┘
                               ▼
                 ┌─────────────────────────────────┐
                 │ Reemplazar reglas específicas   │
                 └─────────────────────────────────┘
                               ▼
                 ┌─────────────────────────────────┐
                 │ Guardar nueva KB optimizada      │
                 └─────────────────────────────────┘

---------------------pseudocódigo---------------------

1. ENVIRONMENT (Pseudocódigo)
 // Clase Grid
CLASS Grid:
    INIT():
        load map structure
        define bushes_area
        define impala_position
        define valid_lion_positions

    FUNCTION distancia(a, b):
        return sqrt((a.x - b.x)^2 + (a.y - b.y)^2)

    FUNCTION en_linea_de_vision(impala, leon):
        IF leon in impala.view_angle AND leon not hidden:
            return TRUE
        ELSE:
            return FALSE

 // Clase Entity (base)
CLASS Entity:
    INIT(x, y, direccion):
        self.x = x
        self.y = y
        self.direccion = direccion
    
    FUNCTION mover(dx, dy):
        self.x += dx
        self.y += dy

 // Clase Impala
CLASS Impala EXTENDS Entity:

    INIT():
        super(impala_x, impala_y, NORTH)
        estado_vision = "frente"
        modo = "aleatorio" OR "programado"
        secuencia_programada = list of actions

    FUNCTION actuar(T):
        IF modo == aleatorio:
            return random action among [ver_izq, ver_der, ver_frente, beber]
        ELSE:
            return secuencia_programada[T % len(secuencia_programada)]

    FUNCTION huir():
        velocidad = T - tiempo_de_huida_iniciado + 1
        mover(velocidad, 0)  # east or west depending direction

 // Clase León
CLASS Leon EXTENDS Entity:

    INIT():
        super(x,y,direccion)
        escondido = FALSE
        atacando = FALSE

    FUNCTION avanzar(hacia_impala):
        mover(1 step towards impala)

    FUNCTION esconderse():
        escondido = TRUE

    FUNCTION atacar():
        atacando = TRUE
        mover(2 steps towards impala)

 // Environment: Ciclo T
CLASS Environment:

    INIT(grid, impala, leon):
        historial = []

    FUNCTION step(T):

        # 1. Impala actúa
        accion_impala = impala.actuar(T)

        # 2. León decide su acción (desde DecisionMaker)
        situacion = construir_situacion()
        accion_leon = decision_maker.decidir(situacion)

        # 3. Ejecutar acciones
        ejecutar_accion_impala(accion_impala)
        ejecutar_accion_leon(accion_leon)

        # 4. Evaluar huida
        IF debe_huir(impala, leon):
            impala.huir()

        # 5. Registrar paso
        historial.append((T, accion_impala, accion_leon, posiciones))

        # 6. Verificar fin de cacería
        IF leon alcanza impala:
            return "exito"
        IF impala supera limites:
            return "fracaso"

        return "continuar"

2. KNOWLEDGE BASE (Reglas + Generalización)
 // Clase Rule
 CLASS Rule:
    INIT(condiciones, accion):
        self.condiciones = condiciones  # dict con valores o sets
        self.accion = accion
        self.confianza = 1

    FUNCTION match(situacion):
        FOR cada atributo en condiciones:
            IF valor_situacion no coincide con valor_condicion:
                return FALSE
        return TRUE

 // Clase KnowledgeBase
 CLASS KnowledgeBase:

    INIT():
        reglas = []

    FUNCTION query(situacion):
        FOR regla IN reglas:
            IF regla.match(situacion):
                return regla.accion
        return NONE  # no match

    FUNCTION add_experience(situacion, accion, resultado):
        regla = Rule(situacion, accion)
        reglas.append(regla)

    FUNCTION generalize():
        FOR cada par de reglas r1, r2:
            IF r1.accion == r2.accion AND son_similares(r1, r2):
                nueva = combinar(r1, r2)
                eliminar r1, r2
                agregar nueva

3. DECISION MAKER
CLASS DecisionMaker:

    INIT(kb):
        self.kb = kb
        ultima_explicacion = ""

    FUNCTION decidir(situacion):

        accion = kb.query(situacion)

        IF accion != NONE:
            ultima_explicacion = "Basado en regla existente"
            return accion

        # Si no hay regla → acción aleatoria en entrenamiento
        accion = random among [avanzar, esconderse, atacar]
        ultima_explicacion = "Acción exploratoria (sin conocimiento previo)"
        return accion

    FUNCTION explicar():
        return ultima_explicacion

4. ENTRENAMIENTO MASIVO
CLASS Trainer:

    INIT(environment, decision_maker, kb):
        self.env = environment
        self.dm = decision_maker
        self.kb = kb

    FUNCTION run(n_incursiones):

        FOR i in range(n_incursiones):

            situar_leon_en(posicion_inicial_random)

            T = 0
            WHILE TRUE:

                resultado = env.step(T)

                situacion = obtener_situacion()
                accion = ultima_accion_leon
                kb.add_experience(situacion, accion, resultado)

                IF resultado == "exito" OR resultado == "fracaso":
                    BREAK

                T += 1

            kb.generalize()

5. CACERÍA PASO A PASO (Modo Usuario)
FUNCTION caceria_paso_a_paso():

    inicializar_entorno()

    PRINT estado_inicial

    T = 0
    WHILE TRUE:

        PRINT "T =", T

        resultado = env.step(T)

        PRINT acciones de impala y leon
        PRINT posiciones

        IF usuario pregunta "¿por qué?":
            PRINT decision_maker.explicar()

        IF resultado != "continuar":
            PRINT "Resultado final:", resultado
            BREAK

        esperar input del usuario ("siguiente paso")
        
        T += 1

6. PERSISTENCIA (Guardar / Cargar KB)
FUNCTION save_KB(filename):
    abrir archivo
    serializar reglas a JSON
    escribir en archivo

FUNCTION load_KB(filename):
    abrir archivo
    leer JSON
    reconstruir reglas en objetos Rule

-------------------Video Demo-------------------

Link del video

-------------------Créditos-------------------

Proyecto realizado por: 
 -Lozano Perez Johan Andres
 -
 -
Curso: Sistemas Inteligentes – FES Acatlán
Profesor: Javier Rosas Hernández
Semestre: 2026-I