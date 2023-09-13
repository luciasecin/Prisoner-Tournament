#Grupo:
#  Lucía Secín (748/19)
#  Pablo Dallegri (445/20)

from Prisoner import Prisoner
from difflib import SequenceMatcher as StrategyMatcher 
import random

# Mastermind onoce algunas estrategias muy basicas de juego  e intenta predecir contra quien esta jugando.
# A veces, le sale muy bien, otras no tanto.

class Mastermind(Prisoner):

    def __init__(self):
        
        self.name="Mastermind" # nombre completo a imprimir
        self.N = 0 # total de rondas hasta ahora
        
        self.possible_strategies = {
            "Disentido": [],
            "Cooperativo": [],
            "Rencoroso": [],
            "Copiador": [],
            "Alternador": []
        }
        
        self.my_strategy = [] # Guarda su historial
        self.other_strategy_history = [] # Guarda historial de estrategias de su oponente
        self.most_similar_strategy = "" # Posible estrategia oponente
        self.most_similar_score = 0
    
    # Calcula la similitud entre el oponente y los que podria ser    
    def calculate_similarity(self):
        
        similarities = {
            "Disentido" : 0,
            "Cooperativo": 0,
            "Rencoroso": 0,
            "Copiador": 0,
            "Alternador": 0
        }
        
        for strategy in self.possible_strategies:
            similarity = StrategyMatcher(None,self.possible_strategies[strategy],self.other_strategy_history).ratio()
            similarities[strategy] = similarity
        
        self.most_similar_strategy = max(similarities, key = similarities.get)
        self.most_similar_score = similarities[self.most_similar_strategy]
            
    # Estrategias de juego de posibles jugadores
    def pick_strategy_opponent(self, player_name):
        pick = True
        if player_name == "Disentido":
            #Siempre Disiente
            pick = False
            
        elif player_name == "Cooperativo":
            #Siempre Coopera
            pick = True
            
        elif player_name == "Rencoroso":
            #Una vez traicionado disiente siempre
            if False in self.my_strategy:
                pick = False
            else:
                pick = True
                
        elif player_name == "Copiador": 
            #Elije mi ultima eleccion
            if self.N > 0:
                pick = self.my_strategy[-1]
            
        elif player_name == "Alternador":
            #Elije el alterno a su ultima eleccion
            if self.N > 0:
                pick = not self.possible_strategies[player_name][-1]
                
        self.possible_strategies[player_name].append(pick)   
    
    # Calcula el movimiento de cada uno de los posibles oponentes y los agrega a su historial
    def other_opponents_pick(self):
        for strategy in self.possible_strategies:
            self.pick_strategy_opponent(strategy)
    
    # Elijo mi estrategia                
    def pick_strategy(self):
        self.calculate_similarity() # Me fijo a que posible oponente se parece mas mi oponente
        
        opponent = self.most_similar_strategy
        opponent_similarity = self.most_similar_score
        pick = True
        
        if self.N < 4: #Randomiza hasta la 5ta jugada para identificar al jugador y luego elige estrategia
            pick = bool(random.getrandbits(1))
            
        elif opponent_similarity < 0.7: # Si no encuentra un oponente similar, elige disentir
            pick = False
            
        else:    
            if opponent == "Disentido":
                # Si nunca coopera, me conviene disentir
                pick = False
                
            elif opponent == "Cooperativo":
                # Si siempre coopera, me conviene siempre disentir
                pick = False
                
            elif opponent == "Rencoroso":
                # La mejor estrategia contra este es cooperar siempre hasta el ultimo movimiento
                # y ahi disentir, pero no sabemos cuantas rondas se juegan
                if False in self.other_strategy_history:
                    pick = False
                else:
                    pick = True
                    
            elif opponent == "Copiador":
                # Pasa lo mismo que con rencoroso, solo que aca despues de poner una falsa me conviene seguir cooperando
                # (en genral)
                if self.N < 99:
                    pick = True 
                else:
                    pick = False
                    
            elif opponent == "Alternador":
                #Si la proxima coopera, me conviene disentir y si la proxima disiente tambien
                pick = False
            
        return pick
    
    # Proceso resultados
    def process_results(self, my_strategy, other_strategy):
        self.other_opponents_pick() # Calculo que habria elegido cada posible oponente
        self.N += 1
        self.other_strategy_history.append(other_strategy) # guardo estrategia del oponente al historial
        self.my_strategy.append(my_strategy) # guardo mi estrategia en mi historial
