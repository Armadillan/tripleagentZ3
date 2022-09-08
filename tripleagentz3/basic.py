from enum import Enum

from z3 import *

class Assumption(Enum):
    VIRUS_NEVER_BACKSTAB = 1
    SERVICE_NEVER_LIE = 2
    I_AM_PLAYING = 2
    SERVICE_NEVER_BACKSTAB = 3
    #Means virus always give Confession to other virus, only applicable to Confession
    VIRUS_DONT_CONFESS = 4

def ExactlyNVirus(player_list, N):
    """player_list does not include Z3"""
    return PbEq([(x,1) for x in player_list], N)

def GetAllModels(solver, player_list):
    """player_list does not include Z3"""
    solver.push()
    models = []
    check = solver.check()
    if check != sat:
        return check
    while check == sat:
        m = solver.model()
        if list(m) == []:
            return []
        models.append(m)
        solver.add(
            Or([X != m[X] for X in player_list])
        )
        check = solver.check()
    solver.pop()
    return models