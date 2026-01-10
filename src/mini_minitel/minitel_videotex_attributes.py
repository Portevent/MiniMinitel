from .C0 import ESC
from .C1 import DOUBLE_HAUTEUR, DOUBLE_GRANDEUR, DOUBLE_LARGEUR, GRANDEUR_NORMALE
from .minitel_videotex import MinitelVideotex


class MinitelVideotexAttributes(MinitelVideotex):
    """
    Minitel Videotex attributes
    """

    def _setAttribute(self, attribute) -> None:
        self._writeByte(ESC)
        self._writeByte(attribute)
        if attribute == DOUBLE_HAUTEUR or attribute == DOUBLE_GRANDEUR:
            self.moveCursorDown(1)
            currentSize = attribute
        elif attribute == GRANDEUR_NORMALE or attribute == DOUBLE_LARGEUR:
            currentSize = attribute

    def setDoubleHauteur(self) -> None:
        self._setAttribute(DOUBLE_HAUTEUR)

    def setDoubleLargeur(self) -> None:
        self._setAttribute(DOUBLE_LARGEUR)

    def setDoubleGrandeur(self) -> None:
        self._setAttribute(DOUBLE_GRANDEUR)

    def setGrandeurNormale(self) -> None:
        self._setAttribute(GRANDEUR_NORMALE)