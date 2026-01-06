
from minitel.minitel_commands import DOUBLE_GRANDEUR, DOUBLE_HAUTEUR, DOUBLE_LARGEUR, FOND_ROUGE, CLIGNOTEMENT, MAJENTA, \
    BLANC, FIXE, GRANDEUR_NORMALE, FOND_JAUNE, LIGNAGE_DEBUT, FOND_INVERSE, MASQUAGE, FOND_NORMAL, DEMASQUAGE
from minitel.minitel_controller import MinitelController

with MinitelController() as minitel:
    minitel.returnToTopLeftAndClearScreen()
    minitel.cursorMoveTo(4, 4)

    minitel._setAttribute(DOUBLE_GRANDEUR)
    minitel._setAttribute(MAJENTA)
    minitel.write("Example")
    minitel._setAttribute(BLANC)
    minitel.write(" text")

    minitel.cursorMoveTo(6, 6)
    minitel._setAttribute(GRANDEUR_NORMALE)
    minitel._setAttribute(CLIGNOTEMENT)
    minitel.write("Hello world")

