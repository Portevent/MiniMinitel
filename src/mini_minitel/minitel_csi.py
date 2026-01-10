from .minitel_videotex_attributes import MinitelVideotexAttributes

class MinitelCSI(MinitelVideotexAttributes):
    """
    Minitel CSI commands
    """

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

    def clearAllAfter(self):
        """
        Clear everything after the cursor till last row (doesn't move cursor)
        """
        self._writeCSI()
        # self._writeByte(b'\x30') Optional, doesn't matter
        self._writeByte(b'\x4A')

    def clearAllBefore(self):
        """
        Clear everything before the cursor till first row (doesn't move cursor)
        """
        self._writeCSI()
        self._writeByte(b'\x31')
        self._writeByte(b'\x4A')

    def clearScreen(self):
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
