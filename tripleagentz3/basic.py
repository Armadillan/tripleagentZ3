from enum import Enum

from z3 import *

class Assumption(Enum):
    VIRUS_NEVER_BACKSTAB = 1
    I_AM_PLAYING = 2
    SERVICE_NEVER_LIE = 2
    SERVICE_NEVER_BACKSTAB = 3

def ExactlyNVirus(player_list, N):
    """player_list does not include Z3"""
    return PbEq([(x,1) for x in player_list], N)

def GetAllModels(solver, player_list):
    """player_list does not include Z3"""
    solver.push()
    models = []
    while solver.check() == sat:
        m = solver.model()
        if list(m) == []:
            return []
        models.append(m)
        solver.add(
            Or([X != m[X] for X in player_list])
        )
    solver.pop()
    return models