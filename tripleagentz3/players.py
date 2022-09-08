"""
Very future work on implementing more factions.
Faction enum would probably eventually be moved into basic
"""
from z3 import *
from abc import ABC, abstractmethod
from enum import Enum

# This should be refactored into two separate enums
# "WinCondition" and "ShowsUpAs"
# players should also have property "original_role" for old photographs
FactionSort, factions = EnumSort("Faction", 
["virus", "service", "rogue",
"triple", "deep", "supsicious",
"service loyalist", "virus loyalist",
"grudge", "infatuated", "scapegoat",
"virus defector", "service defector,",
])
# there is also sleeper agent!
# spy transfer can make it so you dont't know your faction...

class Player(ABC):

    @abstractmethod
    def __init__(self, name):
        self.faction = FactionSort()