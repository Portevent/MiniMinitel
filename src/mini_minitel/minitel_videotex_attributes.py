from .C0 import ESC
from .C1 import DOUBLE_HAUTEUR, DOUBLE_GRANDEUR, DOUBLE_LARGEUR, GRANDEUR_NORMALE, CLIGNOTEMENT, FIXE, FOND_INVERSE, \
    FOND_NORMAL
from .minitel_csi import MinitelCSI


class MinitelVideotexAttributes(MinitelCSI):
    """
    Minitel Videotex attributes
    """

    def _set_attribute(self, attribute) -> None:
        """
        Set attribute
        :param attribute: C1 attribute
        """
        self._write_byte(ESC)
        self._write_byte(attribute)
        if attribute == DOUBLE_HAUTEUR or attribute == DOUBLE_GRANDEUR:
            self.move_cursor_down()

    def set_grandeur_normale(self) -> None:
        """
        Switch to normal-sized characters
        """
        self._set_attribute(GRANDEUR_NORMALE)

    def set_double_hauteur(self) -> None:
        """
        Switch to double row characters
        """
        self._set_attribute(DOUBLE_HAUTEUR)

    def set_double_largeur(self) -> None:
        """
        Switch to double column characters
        """
        self._set_attribute(DOUBLE_LARGEUR)

    def set_double_grandeur(self) -> None:
        """
        Switch to double row and column characters
        """
        self._set_attribute(DOUBLE_GRANDEUR)

    def set_blinking(self) -> None:
        """
        Switch to blinking characters
        """
        self._set_attribute(CLIGNOTEMENT)

    def set_non_blinking(self) -> None:
        """
        Revert to non-blinking characters
        """
        self._set_attribute(FIXE)

    def set_inverted_color(self) -> None:
        """
        Switch to inverted color characters
        """
        self._set_attribute(FOND_INVERSE)

    def set_non_inverted_color(self) -> None:
        """
        Revert to non-inverted color characters
        """
        self._set_attribute(FOND_NORMAL)