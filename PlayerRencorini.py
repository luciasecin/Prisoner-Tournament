from Prisoner import Prisoner

class Rencorini(Prisoner):
  def __init__(self):
    self.name = "Rencorini"
    self.play = True
  
  def pick_strategy(self):
    return self.play
  
  def process_results(self, my_strategy, other_strategy):
    self.play = self.play and other_strategy

