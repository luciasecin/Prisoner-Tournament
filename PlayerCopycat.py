from Prisoner import Prisoner

class Copycat(Prisoner):
  def __init__(self):
    self.name = "Copycat"
    self.play = True
  
  def pick_strategy(self):
    return self.play
  
  def process_results(self, my_strategy, other_strategy):
    self.play = other_strategy

