from z3 import *
from tripleagentz3.operations_functions import *
from tripleagentz3.basic import *
from tripleagentz3.stats import *

Z3 = False
A = Bool("A")
B = Bool("B")
C = Bool("C")
D = Bool("D")
players = [A, B, C, D]
num_virus = 2

s = Solver()

s.add(ExactlyNVirus(players, num_virus))

s.add(SecretIntel(C, Z3, D, False))
s.add(AnonymousTip(D, B, True))
s.add(OldPhotographs(Z3, A, B))
s.add(Confession(B, A, False))
s.add(DanishIntelligence(A, Z3, D))

models, _ = GetAllModels(s, players)
print(models)

percent = PlayerPercentages(models)

print(SortStatDict(percent))

teams=TeamsPercentages(models, 2)

print(SortStatDict(teams))