from Prisoner import Prisoner
import random

class Mayorista(Prisoner):

    def __init__(self):
        self.other_coopera = 0
        self.other_disiente = 0
        self.name = "Mayorista" # nombre completo a imprimir

    def pick_strategy(self):
        return self.other_coopera > self.other_disiente
            
    def process_results(self, my_strategy, other_strategy):
        if other_strategy == True: # si el oponente la última vez cooperó
            self.other_coopera += 1 # incremento la cantidad total de veces que cooperó
        else:
            self.other_disiente += 1
