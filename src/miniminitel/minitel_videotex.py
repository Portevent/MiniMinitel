from .C0 import LF, VT, BS, TAB, CR, RS, FF, US, CAN, BEL, ESC
from .minitelinterfacing import MinitelInterfacing

class MinitelVideotex(MinitelInterfacing):
    """
    Basic Minitel Videotex commands
    """

    def write(self, text: str):
        self._write_byte(bytes(text, encoding="ascii"))

    def shift_cursor_down(self):
        """
        Move cursor down one time
        """
        self._write_byte(LF)

    def shift_cursor_up(self):
        """
        Move cursor right one time
        """
        self._write_byte(VT)

    def shift_cursor_left(self):
        """
        Move cursor left one time
        """
        self._write_byte(BS)

    def shift_cursor_right(self):
        """
        Move cursor left one time
        """
        self._write_byte(TAB)

    def cariage_return(self):
        """
        Move cursor to start of the line (sometimes called Origin)
        """
        self._write_byte(CR)

    def return_to_top_left(self):
        """
        (also called RS) Move cursor to start of first row. Explicit article separator
        """
        self._write_byte(RS)

    def explicit_article_separator(self):
        """
        (also called US) Explicit article separator
        """
        self._write_byte(US)

    def complete_to_end_of_line(self):
        """
        (also called CAN) Write spaces from cursor to end of line (doesn't move cursor)
        """
        self._write_byte(CAN)

    def clear(self): # Clear screen, go to top left, reset attributes
        self._write_byte(FF)

    def ring_bel(self) -> None:
        """
        Do a quick sound
        """
        self._write_byte(BEL)

    def ask_cursor_pos(self):
        """
        Ask current cursor position
        """
        self._write_byte(ESC)
        self._write_byte(b'\x61')
        # TODO : listen to anwser
