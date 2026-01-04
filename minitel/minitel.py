from PIL import Image

from minitel.serial import Serial

GRANDEUR_NORMALE = b'\x4C'
DOUBLE_HAUTEUR   = b'\x4D'
DOUBLE_LARGEUR   = b'\x4E'
DOUBLE_GRANDEUR  = b'\x4F'


class Minitel(Serial):

    def write(self, text: str):
        self._writeByte(bytes(text, encoding="ascii"))

    def writeAt(self, x: int, y: int, text: str):
        self.cursorMove(x, y)
        self._writeByte(bytes(text, encoding="ascii"))

    def cursorOn(self):
        self._writeByte(b'\x11')

    def cursorOff(self):
        self._writeByte(b'\x14')

    def cursorMove(self, x: int, y: int):
        self._writeCSI()
        self._writeBytesP(y)
        self._writeByte(b'\x3B')
        self._writeBytesP(x)
        self._writeByte(b'\x48')

    def clearScreen(self):
        self._writeByte(b'\x0C')

    def teletelModeOn(self):
        self._writeByte(b'\x0E')

    def clear(self):
        self._writeCSI()
        self._writeByte(b'\x32')
        self._writeByte(b'\x4A')

    def _writeESC(self):
        self._writeByte(b'\x1B')

    def _writeCSI(self):
        self._writeByte(b'\x1B')
        self._writeByte(b'\x5B')


    def show_pixel(self, pixel, x: int, y: int):
        self.cursorMove(x, y)
        self._writeByte(pixel)

    def setAttribute(self, attribute):
        self._writeESC()
        self._writeByte(attribute)
        if attribute == DOUBLE_HAUTEUR or attribute == DOUBLE_GRANDEUR:
            self.moveCursorDown(1)
            currentSize = attribute
        elif attribute == GRANDEUR_NORMALE or attribute == DOUBLE_LARGEUR:
            currentSize = attribute
