from .C0 import ESC, Con, Coff, SO, SI
from .serial_connection import SerialConnection

MODE_TELETEL_VIDEOTEX = 0 # Teletel Videotex mode, default when booting Minitel. Use 40 columns display
MODE_TELETEL_MIXTE = 1 # Teletel Mixte mode, can be prompted by the server. Use 80 columns display
MODE_TELEINFORMATIQUE = 2 # Ascii mode, can be prompted by the server or user (Fnct + T then A). Use 80 columns display

class MinitelInterfacing(SerialConnection):
    """
    Basic Minitel interface
    """

    mode = MODE_TELETEL_VIDEOTEX

    def _write_csi(self):
        """
        Send Command Sequence Introducer code, commonly used for prompting command
        :return:
        """
        self._write_byte(ESC)
        self._write_byte(b'\x5B')

    def _videotex_to_mixte(self):
        """
        Switch from VideoTex to Mixte
        """
        self._write_byte(ESC)
        self._write_byte(b'\x3A')
        self._write_byte(b'\x32')
        self._write_byte(b'\x7D')
        # Expect to receive \x13 \x70 ?
        self.mode = MODE_TELETEL_MIXTE

    def _mixte_to_videotex(self):
        """
        Switch from Mixte to VideoTex
        """
        self._write_byte(ESC)
        self._write_byte(b'\x3A')
        self._write_byte(b'\x32')
        self._write_byte(b'\x7E')
        # Expect to receive \x13 \x71 ?
        self.mode = MODE_TELETEL_VIDEOTEX

    def _teletel_to_teleinformatique(self):
        """
        Switch from Teletel (Mixte or VideoTex?) to Teleinformatique
        Can be done by user with Fnct + T then A (or then F for French ASCII)
        """
        self._write_byte(ESC)
        self._write_byte(b'\x3A')
        self._write_byte(b'\x31')
        self._write_byte(b'\x7D')
        # Expect to receive \x1B \x5B \x3F \x7A ?
        self.mode = MODE_TELEINFORMATIQUE

    def _teleinformatique_to_videotex(self):
        """
        Switch from Teleinformatique to VideoTex
        Can be done by user with Fnct + T then V
        """
        self._write_byte(ESC)
        self._write_byte(b'\x5B')
        self._write_byte(b'\x3F')
        self._write_byte(b'\x7B')
        # Expect to receive \x13 \x5E ?
        self.mode = MODE_TELETEL_VIDEOTEX

    def cursor_on(self):
        """
        Display cursor
        """
        self._write_byte(Con)

    def cursor_off(self):
        """
        Hide cursor
        """
        self._write_byte(Coff)

    def switch_to_g1(self): # Display images
        """
        Switch to G1 character table (used for semi graphic display)
        """
        self._write_byte(SO)

    def revert_to_g0(self): # Revert to standard alphanum characters
        """
        Revert to G0 character table (alphanumeric character table)
        """
        self._write_byte(SI)