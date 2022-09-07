from abc import ABC, abstractmethod

from z3 import *

from tripleagentz3.basic import *
from tripleagentz3.stats import *

class Operation(ABC):
    
    @abstractmethod
    def __init__(self, assumptions):
        self.assumptions = assumptions
        if not Assumption.SERVICE_NEVER_LIE in self.assumptions:
            raise MissingAssumption("Logic for service agents lying is not implemented yet.")

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
        if Assumption.SERVICE_NEVER_LIE in self.assumptions:
            # if Assumption.VIRUS_NEVER_BACKSTAB in self.assumptions:
            return Implies(Not(self.player), Xor(self.victim_1, self.victim_2))


if __name__ == "__main__":
    di = DanishIntelligence(True, False, False, (Assumption.SERVICE_NEVER_LIE, Assumption.VIRUS_NEVER_BACKSTAB))
    print(di.expression())