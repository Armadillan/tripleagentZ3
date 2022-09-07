from abc import ABC, abstractmethod

from z3 import *

from tripleagentz3.basic import *
from tripleagentz3.stats import *

class Operation(ABC):
    
    @abstractmethod
    def __init__(self, assumptions):
        self.assumptions = assumptions

    @abstractmethod
    def expression(self):
        pass

class DanishIntelligence(Operation):
    def __init__(self, player, victim_1, victim_2, assumptions):
        self.player = player
        self.victim_1 = victim_1
        self.victim_2 = victim_2
        super().__init__(assumptions)
    
    def expression(self):
        knowledge = []
        if Assumption.SERVICE_NEVER_LIE in self.assumptions:
            knowledge.append(Implies(Not(self.player), Xor(self.victim_1, self.victim_2)))
        if Assumption.SERVICE_NEVER_BACKSTAB in self.assumptions:
            knowledge.append(Implies(Not(self.player), Or(self.victim_1, self.victim_2)))
        if Assumption.VIRUS_NEVER_BACKSTAB in self.assumptions:
            knowledge.append(Implies(self.player), Not(And(self.victim_1, self.victim_2)))

        return And(knowledge)

class AnonymousTip(Operation):
    def __init__(self, player, victim, verdict, assumptions):
        # verdict is True == players says victim is virus
        self.player = player
        self.victim = victim
        self.verdict = verdict
        super().__init__(assumptions)
    
    def expression(self):
        knowledge = []
        if self.verdict:
            if Assumption.SERVICE_NEVER_LIE in self.assumptions or Assumption.SERVICE_NEVER_BACKSTAB in self.assumptions:
                knowledge.append(Implies(Not(self.player), self.victim))
            if Assumption.VIRUS_NEVER_BACKSTAB in self.assumptions:
                knowledge.append(Implies(self.player, Not(self.victim)))
        else:
            if Assumption.SERVICE_NEVER_LIE in self.assumptions or Assumption.SERVICE_NEVER_BACKSTAB in self.assumptions:
                knowledge.append(Implies(Not(self.player), Not(self.victim)))
            if Assumption.VIRUS_NEVER_BACKSTAB in self.assumptions:
                knowledge.append(Implies(self.player, self.victim))
        return And(knowledge)


if __name__ == "__main__":
    di = DanishIntelligence(True, False, False, (Assumption.SERVICE_NEVER_LIE, Assumption.VIRUS_NEVER_BACKSTAB, Assumption.SERVICE_NEVER_BACKSTAB))
    print(di.expression())