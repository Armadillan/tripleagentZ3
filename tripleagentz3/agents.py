from abc import ABC, abstractmethod
from xml.dom.expatbuilder import parseFragmentString

from z3 import *

from tripleagentz3.basic import *
from tripleagentz3.stats import *
from tripleagentz3.operations import *

class Agent(ABC):
    @abstractmethod
    def __init__(self, assumptions):
        self.solver = Solver()
        self.assumptions = assumptions

    @abstractmethod
    def add_info(self):
        pass

    @abstractmethod
    def add_info_call(self):
        pass

    @abstractmethod
    def add_vote_call(self, player, victim):
        pass

    @abstractmethod
    def player_stats(self):
        pass

    @abstractmethod
    def team_stats(self):
        pass
    
    @abstractmethod
    def pick_victims(self, operation):
        pass

    @abstractmethod
    def call_vote(self):
        pass

    @abstractmethod
    def vote(self):
        pass

class ServiceAgent(Agent):
    pass

class VirusAgent(Agent):
    pass
