# Prisoner-Tournament
Presentar un programa en Python (seguramente muy pequeño) que defina un prisionero, que será una clase subclase de Prisoner.

La función que decide la jugada es pick_strategy(self), que devolverá un booleano: True si decide jugar C (colaborar) y False si decide jugar D (disentir).

Una vez jugado, se ejecutará la función process_results(self, my_strategy, other_strategy), donde my_Strategy es la estrategia que el prisionero acaba de elegir y other_Strategy es la que acaba de elegir el rival. Las funciones pueden leer cualquier variable miembro de la clase del prisionero que necesite (ver ejemplo). No se puede usar variables globales.
En __init__(self) se debe inicializar toda variable miembro de la clase que uno vaya a necesitar usar, como la historia de jugadas anteriores (contra el mismo rival), y el nombre del prisionero (string). Se jugará contra un mismo rival entre 100 y 400 veces seguidas, una cantidad aleatoria pero siempre igual, luego contra el otro, y así, la misma cantidad de veces entre cada par de oponentes. Para decidir la jugada, no habrá información de contra quién se está jugando ni las historias de otros ni las historias propias contra oponentes anteriores. Cada vez que se pase a jugar contra un nuevo oponente, se inicializarán las instancias (y sus variables miembros), es decir se llamará al __init__ de nuevo.

En el código no se puede usar bibliotecas o módulos que no vengan con el mismo Python, ni usar archivos externos, ni imprimir nada.
Si el programa no siguiera estos lineamientos, no compilara, diera error al ejecutar, se colgara o tardara un tiempo demasiado largo, casi seguramente será descalificado.
Se utilizará posiblemente la última versión estable de Python.
Mientras se va jugando se irá mostrando los puntajes parciales y al final de todo los ganadores.

Se puede presentar en forma individual o de a dos personas. La aprobación de la tarea consiste en que el programa funcione razonablemente con estos lineamientos (no importando el puntaje obtenido en el torneo).
En caso de fuerza mayor, o algún inconveniente con la máquina o con Python, el torneo podría postergarse.
