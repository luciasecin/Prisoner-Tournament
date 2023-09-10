from Prisoner import Prisoner
import random

# El jugador que siempre coopera, Michael, el lider de los angeles

class Michael(Prisoner):

    def __init__(self):
        self.N = 0 # inicializo el nro. total de rondas hasta ahora
        self.name= "Michael" # nombre completo a imprimir

    def pick_strategy(self):
        return True # Siempre coopero

    def process_results(self, my_strategy, other_strategy):
        self.N += 1