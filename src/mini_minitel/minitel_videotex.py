from .C0 import LF, VT, BS, TAB, CR, RS, FF, US, CAN, BEL, ESC
from .minitel import Minitel

DEL = b'\x7F' # Ctrl + <-

class MinitelVideotex(Minitel):
    """
    Basic Minitel Videotex commands
    """

    def write(self, text: str):
        self._writeByte(bytes(text, encoding="ascii"))

    def shiftCursorDown(self):
        """
        Move cursor down one time
        """
        self._writeByte(LF)

    def shiftCursorUp(self):
        """
        Move cursor right one time
        """
        self._writeByte(VT)

    def shiftCursorLeft(self):
        """
        Move cursor left one time
        """
        self._writeByte(BS)

    def shiftCursorRight(self):
        """
        Move cursor left one time
        """
        self._writeByte(TAB)

    def cariageReturn(self):
        """
        Move cursor to start of the line (sometimes called Origin)
        """
        self._writeByte(CR)

    def returnToTopLeft(self):
        """
        (also called RS) Move cursor to start of first row. Explicit article separator
        """
        self._writeByte(RS)

    def explicitArticleSeparator(self):
        """
        (also called US) Explicit article separator
        """
        self._writeByte(US)

    def completeToEndOfLine(self):
        """
        (also called CAN) Write spaces from cursor to end of line (doesn't move cursor)
        """
        self._writeByte(CAN)

    def clear(self): # Clear screen, go to top left, reset attributes
        self._writeByte(FF)

    def ringBel(self) -> None:
        """
        Do a quick sound
        """
        self._writeByte(BEL)

    def askCursorPos(self):
        """
        Ask current cursor position
        """
        self._writeByte(ESC)
        self._writeByte(b'\x61')
        # TODO : listen to anwser
