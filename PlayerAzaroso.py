from Prisoner import Prisoner
import random


# Literalmente al azar
class Azaroso(Prisoner):
  def __init__(self):
    self.name = "Azaroso"
  
  def pick_strategy(self):
    return random.randint(0,1) == 0
  
  def process_results(self, my_strategy, other_strategy):
    pass

