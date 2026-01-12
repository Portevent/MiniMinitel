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

    def writeDoubleGrandeur(self, text: str):
        self.setDoubleGrandeur()
        self.write(text)
        self.setGrandeurNormale()

    def writeDoubleLargeur(self, text: str):
        self.setDoubleLargeur()
        self.write(text)
        self.setGrandeurNormale()

    def startListening(self, on_read: Callable[[MinitelInput], None]):
        value = self.ser.read_all() # Clear buffer before, usefull to get rid of bootup code
        # print(f"READALL -> {value}")

        while True:
            value = self.ser.read()
            print(f" -> {value}")

            if value == ESC: # Mode téléinformatique
                word = self.ser.read() + self.ser.read()

                match word:
                    case b'OM':
                        on_read(MinitelInput(MinitelCode.ENVOI))

                    case b'OP':
                        on_read(MinitelInput(MinitelCode.SOMMAIRE))

                    case b'OQ':
                        on_read(MinitelInput(MinitelCode.ANNULATION))

                    case b'OR':
                        on_read(MinitelInput(MinitelCode.RETOUR))

                    case b'OS':
                        on_read(MinitelInput(MinitelCode.REPETITION))

                    case b'Om':
                        on_read(MinitelInput(MinitelCode.GUIDE))

                    case b'Ol':
                        on_read(MinitelInput(MinitelCode.CORRECTION))

                    case b'On':
                        on_read(MinitelInput(MinitelCode.SUITE))

                    case b'[A':
                        on_read(MinitelInput(MinitelCode.MOVE_UP))

                    case b'[B':
                        on_read(MinitelInput(MinitelCode.MOVE_DOWN))

                    case b'[C':
                        on_read(MinitelInput(MinitelCode.MOVE_RIGHT))

                    case b'[D':
                        on_read(MinitelInput(MinitelCode.MOVE_LEFT))

                    case b'[H':
                        on_read(MinitelInput(MinitelCode.GO_BACK_UP))

                    case b'[L':
                        on_read(MinitelInput(MinitelCode.INSERT_LINE))

                    case b'[M':
                        on_read(MinitelInput(MinitelCode.SUPPR_LINE))

                    case b'[P':
                        on_read(MinitelInput(MinitelCode.SUPPR_COLUMN))

                    case b'[4':
                        word += self.ser.read()
                        # print(f"INSERT COLUMN {word}")
                        on_read(MinitelInput(MinitelCode.INSERT_COLUMN, word.decode()))

                    case b'[2':
                        word += self.ser.read()
                        # print(f"E.Page {word}")
                        on_read(MinitelInput(MinitelCode.E_Page, word.decode()))

                    case _:
                        on_read(MinitelInput(MinitelCode.UNKNOWN_CODE, word.decode()))

            elif value == Sep: # Mode télétel
                word = self.ser.read()

                match word:
                    case b'A':
                        on_read(MinitelInput(MinitelCode.ENVOI))

                    case b'F':
                        on_read(MinitelInput(MinitelCode.SOMMAIRE))

                    case b'E':
                        on_read(MinitelInput(MinitelCode.ANNULATION))

                    case b'B':
                        on_read(MinitelInput(MinitelCode.RETOUR))

                    case b'C':
                        on_read(MinitelInput(MinitelCode.REPETITION))

                    case b'D':
                        on_read(MinitelInput(MinitelCode.GUIDE))

                    case b'G':
                        on_read(MinitelInput(MinitelCode.CORRECTION))

                    case b'H':
                        on_read(MinitelInput(MinitelCode.SUITE))

                    case b'Y':
                        on_read(MinitelInput(MinitelCode.CONNEXION))

                    case _:
                        on_read(MinitelInput(MinitelCode.UNKNOWN_CODE, word.decode()))
            else:
                # Can't add this check in match, as match value: case BS: will map value onto BS
                if value == BS:
                    on_read(MinitelInput(MinitelCode.BS))  # Ctrl + H
                elif value == LF:
                    on_read(MinitelInput(MinitelCode.LF)) # Ctrl + J
                elif value == CAN:
                    on_read(MinitelInput(MinitelCode.CAN)) # Ctrl + X
                elif value == TAB:
                    on_read(MinitelInput(MinitelCode.TAB)) # Ctrl + I
                else:
                    match value:
                        case b'\x00':
                            on_read(MinitelInput(MinitelCode.BRK)) # Ctrl + Connexion
                        case b'\x7f':
                            on_read(MinitelInput(MinitelCode.DELETE)) # Ctrl + Connexion
                        case b'\r':
                            on_read(MinitelInput(MinitelCode.CARRIAGE_RETURN)) # ENTER
                        case _:
                            on_read(MinitelInput(MinitelCode.TEXT, value.decode()))