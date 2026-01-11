from typing import Callable

from src.mini_minitel.C0 import ESC, BS, LF, CAN, TAB, Sep
from src.mini_minitel.minitel_csi import MinitelCSI

class MinitelController(MinitelCSI):

    def write(self, text: str):
        self._writeByte(bytes(text, encoding="ascii"))

    def writeAt(self, x: int, y: int, text: str):
        self.cursorMoveTo(x, y)
        self.write(text)

    on_read: Callable[[str], None]

    def startListening(self):
        while True:
            value = self.ser.read()
            print(f" -> {value}")

            if value == ESC: # Mode téléinformatique
                word = self.ser.read() + self.ser.read()

                match word:
                    case b'OM':
                        print('ENVOI')

                    case b'OP':
                        print("SOMMAIRE")

                    case b'OQ':
                        print("ANNULATION")

                    case b'OR':
                        print("RETOUR")

                    case b'OS':
                        print("REPETITION")

                    case b'Om':
                        print('GUIDE')

                    case b'Ol':
                        print("CORRECTION")

                    case b'On':
                        print("SUITE")

                    case b'[A':
                        print("MOVE UP")

                    case b'[B':
                        print("MOVE DOWN")

                    case b'[C':
                        print("MOVE RIGHT")

                    case b'[D':
                        print("MOVE LEFT")

                    case b'[H':
                        print("GO BACK UP")

                    case b'[L':
                        print("INSERT LINE")

                    case b'[M':
                        print("SUPPR LINE")

                    case b'[P':
                        print("SUPPR COLUMN")

                    case b'[4':
                        word += self.ser.read()
                        print(f"INSERT COLUMN {word}")

                    case b'[2':
                        word += self.ser.read()
                        print(f"E.Page {word}")

                    case _:
                        print('unknown char: ' + str(word))

            elif value == Sep: # Mode télétel
                word = self.ser.read()

                match word:
                    case b'A':
                        print('ENVOI')

                    case b'F':
                        print("SOMMAIRE")

                    case b'E':
                        print("ANNULATION")

                    case b'B':
                        print("RETOUR")

                    case b'C':
                        print("REPETITION")

                    case b'D':
                        print('GUIDE')

                    case b'G':
                        print("CORRECTION")

                    case b'H':
                        print("SUITE")

                    case b'Y':
                        print("CONNEXION")

                    case _:
                        print('unknown char: ' + str(word))
            else:
                # Can't add this check in match, as match value: case BS: will map value onto BS
                if value == BS:
                    print("BS")  # Ctrl + H
                elif value == LF:
                    print("LF") # Ctrl + J
                elif value == CAN:
                    print("CAN") # Ctrl + X
                elif value == TAB:
                    print("TAB") # Ctrl + I
                else:
                    match value:
                        case b'\x00':
                            print("BRK") # Ctrl + Connexion
                        case b'\x7f':
                            print("DELETE") # Ctrl + Connexion
                        case b'\r':
                            print("CARRIAGE RETURN") # ENTER
                        case _:
                            print(f"Input : ({value.decode()})")