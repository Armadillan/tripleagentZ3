from z3 import *
from tripleagentz3.operations_functions import *
from tripleagentz3.basic import *

Z3 = False
A = Bool("A")
B = Bool("B")
C = Bool("C")
D = Bool("D")
players = [A, B, C, D]
# C & D are virus

s = Solver()

s.add(ExactlyNVirus(players, 2))
s.add(Confession(A, B, False))
s.add(DanishIntelligence(B, A, D))
s.add(OldPhotographs(Z3, C, D))
s.add(AnonymousTip(C, B, False))
s.add(SecretIntel(D, Z3, B, True))

print(GetAllModels(s, [A, B, C, D])[0])
