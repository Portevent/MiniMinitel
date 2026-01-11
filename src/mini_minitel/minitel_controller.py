from typing import Callable

from src.mini_minitel.C0 import ESC, BS, LF, CAN, TAB, Sep
from src.mini_minitel.minitel_csi import MinitelCSI
from src.mini_minitel.minitel_dialog_code import MinitelInput, MinitelCode


class MinitelController(MinitelCSI):

    def write(self, text: str):
        self._writeByte(bytes(text, encoding="ascii"))

    def writeAt(self, x: int, y: int, text: str):
        self.cursorMoveTo(x, y)
        self.write(text)

    on_read: Callable[[MinitelInput], None]

    def startListening(self):
        while True:
            value = self.ser.read()
            print(f" -> {value}")

            if value == ESC: # Mode téléinformatique
                word = self.ser.read() + self.ser.read()

                match word:
                    case b'OM':
                        self.on_read(MinitelInput(MinitelCode.ENVOI))

                    case b'OP':
                        self.on_read(MinitelInput(MinitelCode.SOMMAIRE))

                    case b'OQ':
                        self.on_read(MinitelInput(MinitelCode.ANNULATION))

                    case b'OR':
                        self.on_read(MinitelInput(MinitelCode.RETOUR))

                    case b'OS':
                        self.on_read(MinitelInput(MinitelCode.REPETITION))

                    case b'Om':
                        self.on_read(MinitelInput(MinitelCode.GUIDE))

                    case b'Ol':
                        self.on_read(MinitelInput(MinitelCode.CORRECTION))

                    case b'On':
                        self.on_read(MinitelInput(MinitelCode.SUITE))

                    case b'[A':
                        self.on_read(MinitelInput(MinitelCode.MOVE_UP))

                    case b'[B':
                        self.on_read(MinitelInput(MinitelCode.MOVE_DOWN))

                    case b'[C':
                        self.on_read(MinitelInput(MinitelCode.MOVE_RIGHT))

                    case b'[D':
                        self.on_read(MinitelInput(MinitelCode.MOVE_LEFT))

                    case b'[H':
                        self.on_read(MinitelInput(MinitelCode.GO_BACK_UP))

                    case b'[L':
                        self.on_read(MinitelInput(MinitelCode.INSERT_LINE))

                    case b'[M':
                        self.on_read(MinitelInput(MinitelCode.SUPPR_LINE))

                    case b'[P':
                        self.on_read(MinitelInput(MinitelCode.SUPPR_COLUMN))

                    case b'[4':
                        word += self.ser.read()
                        # print(f"INSERT COLUMN {word}")
                        self.on_read(MinitelInput(MinitelCode.INSERT_COLUMN, str(word)))

                    case b'[2':
                        word += self.ser.read()
                        # print(f"E.Page {word}")
                        self.on_read(MinitelInput(MinitelCode.E_Page, str(word)))

                    case _:
                        self.on_read(MinitelInput(MinitelCode.UNKNOWN_CODE, str(word)))

            elif value == Sep: # Mode télétel
                word = self.ser.read()

                match word:
                    case b'A':
                        self.on_read(MinitelInput(MinitelCode.ENVOI))

                    case b'F':
                        self.on_read(MinitelInput(MinitelCode.SOMMAIRE))

                    case b'E':
                        self.on_read(MinitelInput(MinitelCode.ANNULATION))

                    case b'B':
                        self.on_read(MinitelInput(MinitelCode.RETOUR))

                    case b'C':
                        self.on_read(MinitelInput(MinitelCode.REPETITION))

                    case b'D':
                        self.on_read(MinitelInput(MinitelCode.GUIDE))

                    case b'G':
                        self.on_read(MinitelInput(MinitelCode.CORRECTION))

                    case b'H':
                        self.on_read(MinitelInput(MinitelCode.SUITE))

                    case b'Y':
                        self.on_read(MinitelInput(MinitelCode.CONNEXION))

                    case _:
                        self.on_read(MinitelInput(MinitelCode.UNKNOWN_CODE, str(word)))
            else:
                # Can't add this check in match, as match value: case BS: will map value onto BS
                if value == BS:
                    self.on_read(MinitelInput(MinitelCode.BS))  # Ctrl + H
                elif value == LF:
                    self.on_read(MinitelInput(MinitelCode.LF)) # Ctrl + J
                elif value == CAN:
                    self.on_read(MinitelInput(MinitelCode.CAN)) # Ctrl + X
                elif value == TAB:
                    self.on_read(MinitelInput(MinitelCode.TAB)) # Ctrl + I
                else:
                    match value:
                        case b'\x00':
                            self.on_read(MinitelInput(MinitelCode.BRK)) # Ctrl + Connexion
                        case b'\x7f':
                            self.on_read(MinitelInput(MinitelCode.DELETE)) # Ctrl + Connexion
                        case b'\r':
                            self.on_read(MinitelInput(MinitelCode.CARRIAGE_RETURN)) # ENTER
                        case _:
                            self.on_read(MinitelInput(MinitelCode.TEXT, str(value)))