from z3 import *

# True means is virus
# Z3 is service

# assuming service never lies
# and that virus never incriminate each other

A = Bool("A")
B = Bool("B")
C = Bool("C")
D = Bool("D")

# D and C are virus

s = Solver()

# there are exactly two virus
s.add(
    PbEq([(x, 1) for x in (A, B, C, D)], 2)
)

# A shows confession to B, who says A is Service

s.add(
    Implies(A, B)
)

# B gets danish intelligence and says that A XOR D is virus
s.add(
    Implies(Not(B), Xor(A, D))
)

# Z3 gets old photographs showing C & D being on the same team
s.add(
    Not(Xor(C, D))
)

# C gets anonymous tip and claims that B is service
s.add(
    And(
        Implies(B, C),
        Implies(Not(C), Not(B))
    )
)

# D gets secret intel and calims that at least one of Z3 OR B is virus
# Z3 knows it's not virus
s.add(
    Implies(Not(D), B)
)

while s.check() == sat:
    print(s.model())
    s.add(
        Or(
            A != s.model()[A],
            B != s.model()[B],
            C != s.model()[C],
            D != s.model()[D],
        )
    )