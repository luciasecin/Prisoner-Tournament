from Prisoner import Prisoner
import random

# El jugador que siempre coopera, Michael, el lider de los angeles

class Prueba(Prisoner):

    def __init__(self):
        self.N = 0 # inicializo el nro. total de rondas hasta ahora
        self.name= "Prueba" # nombre completo a imprimir

    def pick_strategy(self):
        if self.N == 0:
            return True
        if self.N == 1:
            return True
        if self.N == 2:
            return True
        if self.N == 3:
            return True
        if self.N == 4:
            return False
        if self.N == 5:
            return True
        if self.N == 6:
            return True
        if self.N == 7:
            return True
        if self.N == 8:
            return True
        if self.N == 9:
            return True

    def process_results(self, my_strategy, other_strategy):
        self.N += 1