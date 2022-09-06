"""
Statistics from list of models
"""

from itertools import combinations

def PlayerPercentages(models_list):
    return {
        player: [model[player] for model in models_list].count(True)/len(models_list)
        for player in models_list[0]
        }

def TeamsPercentages(models_list, num_virus):
    teams = combinations(list(models_list[0]), num_virus)
    out = {}
    for team in teams:
        occurances = 0
        for model in models_list:
            if all([model[x] for x in team]):
                occurances += 1
        out[team] = occurances/len(models_list)
        
    return out