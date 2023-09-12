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
from PlayerMastermind import Mastermind
from PlayerPrueba import Prueba

from collections import Counter

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
    if (p2.name == "Mastermind" or p2.name == "Mastermind"):
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
  first = []
  second = []
  third =[]
  fourth = []
  for iter in range(10):
    print("\n----------------Ronda", iter, "-------------\n")
    competing = [Alterneitor, Jajas, Rencorini, Copycat, Lucifer, Michael, Azaroso, Mayorista, Proba, Mastermind]
    #competing = [Alterneitor, Rencorini, Copycat, Lucifer, Michael, Mastermind]
    t = Tournament(competing,200)
    t.round_robin()
    
    # Log
    d = {}
    for i in range(len(competing)):
      d[competing[i]().name] = t.scores[i]
    for (name, score) in sorted(d.items(), key=lambda item: -item[1]):
      print(f'{name:{t.print_padding}} | {score}')
    
    first.append(sorted(d.items(), key=lambda item: -item[1])[0][0])
    second.append(sorted(d.items(), key=lambda item: -item[1])[1][0])
    third.append(sorted(d.items(), key=lambda item: -item[1])[2][0])
    fourth.append(sorted(d.items(), key=lambda item: -item[1])[3][0])
  
  print("---------------Final: 10 Competidores---------------")  
  print("---------------100 rondas de 150---------------------") 
  print("Primero:",Counter(first)["Mastermind"])
  print("Segundo:",Counter(second)["Mastermind"])
  print("Tercero:",Counter(third)["Mastermind"])
  print("Cuarto:",Counter(fourth)["Mastermind"])

run()
