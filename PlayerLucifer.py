from Prisoner import Prisoner
import random

# El jugador que nunca coopera, Lucifer, el rey del infierno

class Lucifer(Prisoner):

    def __init__(self):
        self.N = 0 # inicializo el nro. total de rondas hasta ahora
        self.name= "Lucifer" # nombre completo a imprimir

    def pick_strategy(self):
        return False # Nunca coopero

    def process_results(self, my_strategy, other_strategy):
        self.N += 1