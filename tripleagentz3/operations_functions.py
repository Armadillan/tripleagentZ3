"""
DEPRECATED in favour of tripleagentz3.operations.
Will be removed at some point.

Creates z3 expressions for each operation
assumes service never lies
and virus never incriminate each other
if Z3 is playing, pass False as player
"""
from warnings import warn

from z3 import *

warn("tripleagentz3.operations_functions is deprecated in favour of tripleagentz3.operations. This module will be removed at some point.", FutureWarning, stacklevel=2)

def Confession(player, victim, verdict):
    if verdict:
        return And(
            Implies(victim, Not(player)),
            Implies(Not(victim), player)
        )
    else:
        return And(
            Implies(player, victim),
            Implies(Not(victim), Not(player))
        )

def SecretIntel(player, victim_1, victim_2, verdict):
    # verdict == True means player claims at least one of victim_1 OR victim_2 is virus
    if verdict:
        return Implies(Not(player), Or(victim_1, victim_2))
    else:
        return Implies(Not(player), And(Not(victim_1),Not(victim_2)))

def OldPhotographs(player, victim_1, victim_2):
    return Implies(Not(player), Not(Xor(victim_1, victim_2)))

def DanishIntelligence(player, victim_1, victim_2):
    return Implies(Not(player), Xor(victim_1, victim_2))

def AnonymousTip(player, victim, verdict):
    # verdict is True == players says victim is virus
    if verdict:
        return Implies(Not(player), victim)
    else:
        # player says victim is not virus
        return And(
            Implies(victim, player),
            Implies(Not(player), Not(victim))
        )
