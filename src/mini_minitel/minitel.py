from .C0 import ESC, Con, Coff, FF, SO, SI
from .serial_connection import SerialConnection

MODE_TELETEL_VIDEOTEX = 0 # Teletel Videotex mode, default when booting Minitel. Use 40 columns display
MODE_TELETEL_MIXTE = 1 # Teletel Mixte mode, can be prompted by the server. Use 80 columns display
MODE_TELEINFORMATIQUE = 2 # Ascii mode, can be prompted by the server or user (Fnct + T then A). Use 80 columns display

class Minitel(SerialConnection):
    """
    Basic Minitel interface
    """

    mode = MODE_TELETEL_VIDEOTEX

    def _writeCSI(self):
        """
        Send Command Sequence Introducer code, commonly used for prompting command
        :return:
        """
        self._writeByte(ESC)
        self._writeByte(b'\x5B')

    def _videotex_to_mixte(self):
        """
        Switch from VideoTex to Mixte
        """
        self._writeByte(ESC)
        self._writeByte(b'\x3A')
        self._writeByte(b'\x32')
        self._writeByte(b'\x7D')
        # Expect to receive \x13 \x70 ?
        self.mode = MODE_TELETEL_MIXTE

    def _mixte_to_videotex(self):
        """
        Switch from Mixte to VideoTex
        """
        self._writeByte(ESC)
        self._writeByte(b'\x3A')
        self._writeByte(b'\x32')
        self._writeByte(b'\x7E')
        # Expect to receive \x13 \x71 ?
        self.mode = MODE_TELETEL_VIDEOTEX

    def _teletel_to_teleinformatique(self):
        """
        Switch from Teletel (Mixte or VideoTex?) to Teleinformatique
        Can be done by user with Fnct + T then A (or then F for French ASCII)
        """
        self._writeByte(ESC)
        self._writeByte(b'\x3A')
        self._writeByte(b'\x31')
        self._writeByte(b'\x7D')
        # Expect to receive \x1B \x5B \x3F \x7A ?
        self.mode = MODE_TELEINFORMATIQUE

    def _teleinformatique_to_videotex(self):
        """
        Switch from Teleinformatique to VideoTex
        Can be done by user with Fnct + T then V
        """
        self._writeByte(ESC)
        self._writeByte(b'\x5B')
        self._writeByte(b'\x3F')
        self._writeByte(b'\x7B')
        # Expect to receive \x13 \x5E ?
        self.mode = MODE_TELETEL_VIDEOTEX

    def cursorOn(self):
        self._writeByte(Con)

    def cursorOff(self):
        self._writeByte(Coff)

    def switchToG1(self): # Display images
        self._writeByte(SO)

    def revertToG0(self): # Revert to standart alphanum characters
        self._writeByte(SI)