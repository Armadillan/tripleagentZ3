from z3 import *

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