from Prisoner import Prisoner

#Cambia en cada partida al opuesto de lo que hizo la partida anterior
class Alterneitor(Prisoner):
  def __init__(self):
    self.name = "Alterneitor"
    self.play = True
  
  def pick_strategy(self):
    return self.play
  
  def process_results(self, my_strategy, other_strategy):
    self.play = not my_strategy
