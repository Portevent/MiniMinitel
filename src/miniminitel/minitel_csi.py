from .minitel_videotex import MinitelVideotex

class MinitelCSI(MinitelVideotex):
    """
    Minitel CSI commands
    Command Sequence Introducer
    """

    def move_cursor_up(self, n: int = 1):
        """
        Move cursor up n time
        Note : when n = 1, this function is similar to shiftCursorUp()
        """
        self._write_csi()
        self._write_bytes_p(n)
        self._write_byte(b'\x41')

    def move_cursor_down(self, n: int = 1):
        """
        Move cursor down n time
        Note : when n = 1, this function is similar to shiftCursorDown()
        """
        self._write_csi()
        self._write_bytes_p(n)
        self._write_byte(b'\x42')

    def move_cursor_right(self, n: int = 1):
        """
        Move cursor right n time
        Note : when n = 1, this function is similar to shiftCursorRight()
        """
        self._write_csi()
        self._write_bytes_p(n)
        self._write_byte(b'\x43')

    def move_cursor_left(self, n: int = 1):
        """
        Move cursor left n time
        Note : when n = 1, this function is similar to shiftCursorLeft()
        """
        self._write_csi()
        self._write_bytes_p(n)
        self._write_byte(b'\x44')

    def cursor_move_to(self, x: int, y: int):
        """
        Move cursor to row X and column Y
        :param x: from 01 to 24
        :param y: from 01 to 40 (or 80)
        """
        self._write_csi()
        self._write_bytes_p(y)
        self._write_byte(b'\x3B')
        self._write_bytes_p(x)
        self._write_byte(b'\x48')

    def clear_all_after(self):
        """
        Clear everything after the cursor till last row (doesn't move cursor)
        """
        self._write_csi()
        # self._writeByte(b'\x30') Optional, doesn't matter
        self._write_byte(b'\x4A')

    def clear_all_before(self):
        """
        Clear everything before the cursor till first row (doesn't move cursor)
        """
        self._write_csi()
        self._write_byte(b'\x31')
        self._write_byte(b'\x4A')

    def clear_screen(self):
        """
        Clear everything (doesn't move cursor)
        """
        self._write_csi()
        self._write_byte(b'\x32')
        self._write_byte(b'\x4A')

    def clear_row_end(self):
        """
        Clear after the cursor till the end of row (doesn't move cursor)
        """
        self._write_csi()
        # self._writeByte(b'\x30') Optional
        self._write_byte(b'\x4B')

    def clear_row_start(self):
        """
        Clear before the cursor till the start of row (doesn't move cursor)
        """
        self._write_csi()
        self._write_byte(b'\x31')
        self._write_byte(b'\x4B')

    def clear_row(self):
        """
        Clear current row (doesn't move cursor)
        """
        self._write_csi()
        self._write_byte(b'\x32')
        self._write_byte(b'\x4B')

    def insert_rows(self, count: int):
        """
        Insert n rows
        """
        self._write_csi()
        self._write_bytes_p(count)
        self._write_byte(b'\x4C')

    def clear_rows(self, count: int):
        """
        Clear n rows
        """
        self._write_csi()
        self._write_bytes_p(count)
        self._write_byte(b'\x4D')

    def clear_characters(self, count: int):
        """
        Clear n character
        """
        self._write_csi()
        self._write_bytes_p(count)
        self._write_byte(b'\x50')

    def insert_mode_on(self):
        """
        Activate insertion mode
        """
        self._write_csi()
        self._write_byte(b'\x34')
        self._write_byte(b'\x68')

    def insert_mode_off(self):
        """
        Deactivate insertion mode
        """
        self._write_csi()
        self._write_byte(b'\x34')
        self._write_byte(b'\x6C')
