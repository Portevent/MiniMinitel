from PIL import Image

from minitel.minitel import Minitel
from minitel.serial import Serial

GRANDEUR_NORMALE = b'\x4C'
DOUBLE_HAUTEUR   = b'\x4D'
DOUBLE_LARGEUR   = b'\x4E'
DOUBLE_GRANDEUR  = b'\x4F'

# Palette Minitel (8 couleurs) en RGB
minitel_palette = [
    (0, 0, 0),  # Noir
    (255, 0, 0),  # Rouge
    (0, 255, 0),  # Vert
    (255, 255, 0),  # Jaune
    (0, 0, 255),  # Bleu
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 255, 255)  # Blanc
]

pixel_to_g1_code = {
    "000000": "20", "100000": "21", "010000": "22", "110000": "23",
    "001000": "24", "101000": "25", "011000": "26", "111000": "27",
    "000100": "28", "100100": "29", "010100": "2A", "110100": "2B",
    "001100": "2C", "101100": "2D", "011100": "2E", "111100": "2F",
    "000010": "30", "100010": "31", "010010": "32", "110010": "33",
    "001010": "34", "101010": "35", "011010": "36", "111010": "37",
    "000110": "38", "100110": "39", "010110": "3A", "110110": "3B",
    "001110": "3C", "101110": "3D", "011110": "3E", "111110": "3F",
    "000001": "60", "100001": "61", "010001": "62", "110001": "63",
    "001001": "64", "101001": "65", "011001": "66", "111001": "67",
    "000101": "68", "100101": "69", "010101": "6A", "110101": "6B",
    "001101": "6C", "101101": "6D", "011101": "6E", "111101": "6F",
    "000011": "70", "100011": "71", "010011": "72", "110011": "73",
    "001011": "74", "101011": "75", "011011": "76", "111011": "77",
    "000111": "78", "100111": "79", "010111": "7A", "110111": "7B",
    "001111": "7C", "101111": "7D", "011111": "7E", "111111": "7F"
}

color_codes = {
    (0, 0, 0):       ("1B40", "1B50"),
    (255, 0, 0):     ("1B41", "1B51"),
    (0, 255, 0):     ("1B42", "1B52"),
    (255, 255, 0):   ("1B43", "1B53"),
    (0, 0, 255):     ("1B44", "1B54"),
    (255, 0, 255):   ("1B45", "1B55"),
    (0, 255, 255):   ("1B46", "1B56"),
    (255, 255, 255): ("1B47", "1B57")
}

class MinitelController(Minitel):

    def write(self, text: str):
        self._writeByte(bytes(text, encoding="ascii"))

    def writeAt(self, x: int, y: int, text: str):
        self.cursorMove(x, y)
        self._writeByte(bytes(text, encoding="ascii"))

    def show_pixel(self, pixel, x: int, y: int):
        self.cursorMove(x, y)
        self._writeByte(pixel)

    def setAttribute(self, attribute):
        self._writeESC()
        self._writeByte(attribute)

        if attribute == DOUBLE_HAUTEUR or attribute == DOUBLE_GRANDEUR:
            # self.moveCursorDown(1)
            currentSize = attribute
        elif attribute == GRANDEUR_NORMALE or attribute == DOUBLE_LARGEUR:
            currentSize = attribute
