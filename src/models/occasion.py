from enum import Enum

class Occasion(str, Enum):
    FESTIVE = "festive"
    WORK = "work"
    PARTY = "party"
    ACTIVE = "active"
    CASUAL = "casual"

