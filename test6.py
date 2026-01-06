
from minitel.minitel_commands import Minitel, DOUBLE_GRANDEUR, DOUBLE_HAUTEUR, DOUBLE_LARGEUR, FOND_ROUGE, CLIGNOTEMENT, MAJENTA, \
    BLANC, FIXE, GRANDEUR_NORMALE, FOND_JAUNE, LIGNAGE_DEBUT, FOND_INVERSE, MASQUAGE, FOND_NORMAL, DEMASQUAGE
from minitel.minitel_controller import MinitelController

with MinitelController() as minitel:
    minitel.clear()
    minitel.explicitArticleSeparator()
    minitel.setAttribute(FOND_NORMAL)
    minitel.setAttribute(FIXE)
    minitel.setAttribute(DOUBLE_GRANDEUR)
    minitel.write("Example")
    minitel.write(" text")

    minitel.moveCursorDown()
    minitel.cariageReturn()
    minitel.setAttribute(GRANDEUR_NORMALE)
    minitel.setAttribute(CLIGNOTEMENT)
    minitel.write(" Hello world")

