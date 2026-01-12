from typing import Callable

from src.mini_minitel.C0 import ESC, BS, LF, CAN, TAB, Sep
from src.mini_minitel.minitel_dialog_code import MinitelInput, MinitelCode
from src.mini_minitel.minitel_videotex_attributes import MinitelVideotexAttributes


class MinitelController(MinitelVideotexAttributes):

    def write(self, text: str):
        """
        Write text on Minitel
        :param text: text
        """
        self._write_byte(bytes(text, encoding="ascii"))

    def write_at(self, x: int, y: int, text: str) -> None:
        """
        Move cursor to position and write to
        :param x: Column
        :param y: Row
        :param text: Text
        """
        self.cursor_move_to(x, y)
        self.write(text)

    def write_double_grandeur(self, text: str) -> None:
        """
        Write with double grandeur
        :param text: Text
        """
        self.set_double_grandeur()
        self.write(text)
        self.set_grandeur_normale()

    def write_double_largeur(self, text: str):
        """
        Write with double largeur
        :param text: Text
        """
        self.set_double_largeur()
        self.write(text)
        self.set_grandeur_normale()

    def write_double_hauteur(self, text: str):
        """
        Write with double hauteur
        :param text: Text
        """
        self.set_double_hauteur()
        self.write(text)
        self.set_grandeur_normale()

    def start_listening(self, on_read: Callable[[MinitelInput], None]):
        """
        Listen to port and pass MinitelInput to callback
        :param on_read: Action to perform on read
        """
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