from Prisoner import Prisoner
import random

class Proba(Prisoner):

    def __init__(self):
        self.N = 0 # numero de jugadas
        self.other_coopera = 0
        self.other_disiente = 0
        self.name = "Proba" # nombre completo a imprimir

    def pick_strategy(self):
        if self.N == 0:
            return True
        
        prob_cooperar = self.other_coopera*100/self.N
        prob_disentir = self.other_disiente*100/self.N
        
        return random.choices([True, False], weights= (prob_cooperar, prob_disentir), k = 1)[0]
            
    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        if other_strategy == True: # si el oponente la última vez cooperó
            self.other_coopera += 1 # incremento la cantidad total de veces que cooperó
        else:
            self.other_disiente += 1
