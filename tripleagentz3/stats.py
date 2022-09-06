"""
Statistics from list of models
"""

def PlayerPercentages(models_list):
    return {
        player: [model[player] for model in models_list].count(True)/len(models_list)
        for player in models_list[0]
        }

def TeamsPercentages(models_list):
    return