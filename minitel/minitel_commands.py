from .minitel import Minitel

BS = b'\x08' # Ctrl + H     Move cursor left
TAB = b'\x09' # Ctrl + I    Move cursor right
HT = b'\x09' # Ctrl + I     Move cursor right
LF = b'\x0A' # Ctrl + J     Move cursor down
VT = b'\x0B' # Ctrl + K     Move cursor up
DEL = b'\x7F' # Ctrl + <-
CAN = b'\x18' # Ctrl + X    Add space till end of line
CR = b'\x0D' # <--'         Move cursor to origin
RS = b'\x1E' #              Return cursor to start of first line. Explicit article separator
US = b'\x1F' #              Explicit article separator
FF = b'\x0C' #              Return cursor to start of first line. Clear all. Explicit article separator
BEL = b'\x07' #             Ring a bell

# http://543210.free.fr/TV/stum1b.pdf - page 92 (95 in pdf)
MAJENTA = b'\x45'
BLANC = b'\x47'
CLIGNOTEMENT = b'\x48'
FIXE = b'\x49'
GRANDEUR_NORMALE = b'\x4C'
DOUBLE_HAUTEUR   = b'\x4D'
DOUBLE_LARGEUR   = b'\x4E'
DOUBLE_GRANDEUR  = b'\x4F'
FOND_ROUGE = b'\x51'
FOND_JAUNE = b'\x53'
LIGNAGE_DEBUT = b'\x5A'
MASQUAGE = b'\x58'
LIGNAGE_FIN = b'\x59'
FOND_NORMAL = b'\x5C'
FOND_INVERSE = b'\x5D'
DEMASQUAGE = b'\x5F'

class MinitelCommands(Minitel):
    """
    Basic Minitel commands
    """

    #################
    # region VIDEOTEX
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

    def moveCursorUp(self, n: int = 1):
        """
        Move cursor up n time
        Note : when n = 1, this function is similar to shiftCursorUp()
        """
        self._writeCSI()
        self._writeBytesP(n)
        self._writeByte(b'\x41')

    def moveCursorDown(self, n: int = 1):
        """
        Move cursor down n time
        Note : when n = 1, this function is similar to shiftCursorDown()
        """
        self._writeCSI()
        self._writeBytesP(n)
        self._writeByte(b'\x42')

    def moveCursorRight(self, n: int = 1):
        """
        Move cursor right n time
        Note : when n = 1, this function is similar to shiftCursorRight()
        """
        self._writeCSI()
        self._writeBytesP(n)
        self._writeByte(b'\x43')

    def moveCursorLeft(self, n: int = 1):
        """
        Move cursor left n time
        Note : when n = 1, this function is similar to shiftCursorLeft()
        """
        self._writeCSI()
        self._writeBytesP(n)
        self._writeByte(b'\x44')

    def cursorMoveTo(self, x: int, y: int):
        """
        Move cursor to row X and column Y
        :param x: from 01 to 24
        :param y: from 01 to 40 (or 80)
        """
        self._writeCSI()
        self._writeBytesP(y)
        self._writeByte(b'\x3B')
        self._writeBytesP(x)
        self._writeByte(b'\x48')

    def returnToTopLeft(self):
        """
        (also called RS) Move cursor to start of first row. Explicit article separator
        """
        self._writeByte(RS)

    def returnToTopLeftAndClearScreen(self):
        """
        (also called FF) Move cursor to start of first row. Clear screen. Explicit article separator
        """
        self._writeByte(FF)

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

    def clearAllAfter(self):
        """
        Clear everything after the cursor till last row (doesn't move cursor)
        """
        self._writeCSI()
        # self._writeByte(b'\x30') Optional
        self._writeByte(b'\x4A')

    def clearAllBefore(self):
        """
        Clear everything before the cursor till first row (doesn't move cursor)
        """
        self._writeCSI()
        self._writeByte(b'\x31')
        self._writeByte(b'\x4A')

    def clear(self):
        """
        Clear everything (doesn't move cursor)
        """
        self._writeCSI()
        self._writeByte(b'\x32')
        self._writeByte(b'\x4A')

    def clearRowEnd(self):
        """
        Clear after the cursor till the end of row (doesn't move cursor)
        """
        self._writeCSI()
        # self._writeByte(b'\x30') Optional
        self._writeByte(b'\x4B')

    def clearRowStart(self):
        """
        Clear before the cursor till the start of row (doesn't move cursor)
        """
        self._writeCSI()
        self._writeByte(b'\x31')
        self._writeByte(b'\x4B')

    def clearRow(self):
        """
        Clear current row (doesn't move cursor)
        """
        self._writeCSI()
        self._writeByte(b'\x32')
        self._writeByte(b'\x4B')

    def insertRows(self, count: int):
        """
        Insert n rows
        """
        self._writeCSI()
        self._writeBytesP(count)
        self._writeByte(b'\x4C')

    def clearRows(self, count: int):
        """
        Clear n rows
        """
        self._writeCSI()
        self._writeBytesP(count)
        self._writeByte(b'\x4D')

    def clearCharacters(self, count: int):
        """
        Clear n character
        """
        self._writeCSI()
        self._writeBytesP(count)
        self._writeByte(b'\x50')

    def insertModeOn(self):
        """
        Activate insertion mode
        """
        self._writeCSI()
        self._writeByte(b'\x34')
        self._writeByte(b'\x68')

    def insertModeOff(self):
        """
        Deactivate insertion mode
        """
        self._writeCSI()
        self._writeByte(b'\x34')
        self._writeByte(b'\x6C')

    def ringBel(self):
        """
        Do a quick sound
        """
        self._writeByte(BEL)

    def askCursorPos(self):
        """
        Ask current cursor position
        """
        self._writeESC()
        self._writeByte(b'\x61')
        # TODO : listen to anwser

    def _setAttribute(self, attribute):
        self._writeESC()
        self._writeByte(attribute)
        if attribute == DOUBLE_HAUTEUR or attribute == DOUBLE_GRANDEUR:
            self.moveCursorDown(1)
            currentSize = attribute
        elif attribute == GRANDEUR_NORMALE or attribute == DOUBLE_LARGEUR:
            currentSize = attribute
