from z3 import *
from tripleagentz3.operations_functions import *
from tripleagentz3.basic import *
from tripleagentz3.stats import *

Z3 = False
A = Bool("A")
B = Bool("B")
C = Bool("C")
players = [A, B, C]

s = Solver()

s.add(ExactlyNVirus(players, 2))

s.add(AnonymousTip(B, A, True))
s.add(AnonymousTip(B, C, True))
s.add(AnonymousTip(C, A, True))
s.add(AnonymousTip(C, B, True))
s.add(AnonymousTip(A, B, False))
s.add(AnonymousTip(A, C, False))

#equivalent to just "s.add(A)"

models = GetAllModels(s, players)
print(models)

percent = PlayerPercentages(models)

print(SortStatDict(percent))

teams=TeamsPercentages(models, 2)

print(SortStatDict(teams))
