# C0 grid

# http://543210.free.fr/TV/stum1b.pdf - page 92 (95 in pdf)

NUL : bytes = b'\x00' #             Documentation required
SCH : bytes = b'\x01' #             Documentation required


EOT : bytes = b'\x04' #             Documentation required
ENQ : bytes = b'\x05' #             Documentation required

BEL : bytes = b'\x07' #             Ring a bell
BS : bytes = b'\x08' # Ctrl + H     Move cursor left
HT : bytes = b'\x09' # Ctrl + I     Move cursor right
TAB : bytes = HT     # HT is sometimes called TAB
LF : bytes = b'\x0A' # Ctrl + J     Move cursor down
VT : bytes = b'\x0B' # Ctrl + K     Move cursor up
FF : bytes = b'\x0C' #              Return cursor to start of first line. Clear all. Explicit article separator
CR : bytes = b'\x0D' # <--'         Move cursor to origin
SO : bytes = b'\x0E' #              Switch to G1 characters
SI : bytes = b'\x0F' #              Revert to standart alphanum characters (G0)

DLE : bytes = b'\x10' #              Documentation required
Con : bytes = b'\x11' #              Cursor on
Rep : bytes = b'\x12' #              Documentation required
Sep : bytes = b'\x13' #              Documentation required
Coff : bytes = b'\x14' #              Cursor off
NACK : bytes = b'\x15' #              Documentation required
SYN : bytes = b'\x16' #              Documentation required

CAN : bytes = b'\x18' # Ctrl + X    Add space till end of line
SS2 : bytes = b'\x19' #              Documentation required
SUB : bytes = b'\x1A' #              Documentation required
ESC : bytes = b'\x1B' #              Esc code (used to access C1 grid)
SS3 : bytes = b'\x1D' #              Documentation required
RS : bytes = b'\x1E' #              Return cursor to start of first line. Explicit article separator

US : bytes = b'\x1F' #              Explicit article separator

