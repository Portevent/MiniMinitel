from random import random

from minitel.minitel import Minitel

def pseudo_random(variation: int, centered: float):
    return -4 + (int (variation * random() ** centered))

with Minitel() as minitel:
    minitel.clear()
    while True:
        minitel.writeAt(30 + pseudo_random(8, 10), 11, "       Remember our promise       ")