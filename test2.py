from random import random

from minitel.minitel_controller import MinitelController


def pseudo_random(variation: int, centered: float):
    return -4 + (int (variation * random() ** centered))

with MinitelController() as minitel:
    minitel.clear()
    minitel._teletel_to_teleinformatique()
    while True:
        minitel.writeAt(30 + pseudo_random(8, 10), 11, "       Remember our promise       ")