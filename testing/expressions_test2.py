from itertools import combinations

from z3 import *
from tripleagentz3.operations import *
from tripleagentz3.basic import GetAllModels
from tripleagentz3.stats import *

Z3 = False
A = Bool("A")
B = Bool("B")
C = Bool("C")
D = Bool("D")
players = [A, B, C, D]
# C & D are virus

s = Solver()

s.add(ExactlyNVirus(players, 2))

s.add(OldPhotographs(D, C, Z3))
s.add(Confession(Z3, D, False))
s.add(SecretIntel(B, Z3, D, True))
s.add(AnonymousTip(A, Z3, False))
s.add(DanishIntelligence(C, A, Z3))

models = GetAllModels(s, players)
print(models)

percent = PlayerPercentages(models)

print(percent)
