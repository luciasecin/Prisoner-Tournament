from itertools import combinations
from random import shuffle
import random

from Prisoner import Prisoner

from PlayerAlterneitor import Alterneitor
from PlayerAzaroso import Azaroso
from PlayerCopycat import Copycat
from PlayerLucifer import Lucifer
from PlayerMichael import Michael
from PlayerJajas import Jajas
from PlayerRencorini import Rencorini
from PlayerMayorista import Mayorista
from PlayerProba import Proba

"""
Prisoners' dilemma tournament
"""
class Tournament():
  def __init__(self, competing, n_rounds):
    self.competing = competing
    self.scores = len(competing)*[0]
    self.n_rounds = n_rounds
    self.print_padding = max(map(lambda c: len(c().name), competing))
  
  def score(self, strategy1, strategy2):
    if strategy1 and strategy2:
      return (1, 1)
    elif not strategy1 and strategy2:
      return (2, -1)
    elif strategy1 and not strategy2:
      return (-1, 2)
    else:
      return (0, 0)
  
  def play_match(self, player1, player2):
    # Initialize
    p1 = player1()
    p2 = player2()    
    score1 = 0
    score2 = 0
    history1 = ''
    history2 = ''

    # Play rounds
    for n in range(self.n_rounds):
      (s1, s2) = (p1.pick_strategy(), p2.pick_strategy())
      p1.process_results(s1, s2)
      p2.process_results(s2, s1)
      
      scores = self.score(s1, s2)
      score1 += scores[0]
      score2 += scores[1]
      
      history1 += 'C' if s1 else '-'
      history2 += 'C' if s2 else '-'
    
    # Log
    if (True):
      print(f'{p1.name:{self.print_padding}} | {history1} | {score1}')
      print(f'{p2.name:{self.print_padding}} | {history2} | {score2}')
      print()
    
    # Return scores
    return (score1, score2)


  def round_robin(self):
    matches = list(combinations(range(len(self.competing)), 2))

    # Play all matches
    for match in matches:
      (match_score1, match_score2) = self.play_match(
        self.competing[match[0]],
        self.competing[match[1]])
      self.scores[match[0]] += match_score1
      self.scores[match[1]] += match_score2
  
def run():
  # Compete
  competing = [Alterneitor, Jajas, Rencorini, Copycat, Lucifer, Michael, Azaroso, Mayorista, Proba]
  t = Tournament(competing,100)
  t.round_robin()
  
  # Log
  d = {}
  for i in range(len(competing)):
    d[competing[i]().name] = t.scores[i]
  for (name, score) in sorted(d.items(), key=lambda item: -item[1]):
    print(f'{name:{t.print_padding}} | {score}')
  
run()