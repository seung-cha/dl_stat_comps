from .stats_base import *
from .char_stats import *


# https://deadlock.wiki/Damage_Resistance
def add_multiplicative(stat, a):
    return 1 - (1 - stat) * (1 - a)
