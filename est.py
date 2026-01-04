from minitel.minitel import Minitel

with Minitel() as minitel:
    for i in range(1, 40):
        for j in range(1, 20):

            # minitel.clear()
            minitel.cursorMove(i, j)
            minitel.write(" Zouze de love")
