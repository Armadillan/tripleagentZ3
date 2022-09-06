"""
Creates z3 expressions for each operation

assumes service never lies
and virus never incriminate each other

if Z3 is playing, pass False as player
"""

from z3 import *

from basic import ExactlyNVirus

def Confession(player, victim, verdict):
    if verdict:
        return Or(
            And(player, Not(victim)),
            And(Not(player), victim)
        )
    else:
        return Or(
            And(player, victim),
            And(Not(player), Not(victim))
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
