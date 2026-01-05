import serial


class SerialConnection:
    """
    Raw SerialConnection interface
    """

    def __init__(self, baudrate=4800):
        self.ser = serial.Serial('/dev/ttyUSB0', baudrate=baudrate, bytesize=7, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ser.close()

    def _writeByte(self, byte: bytes):
        self.ser.write(byte)

    def _writeWord(self, bits: bytes):
        self._writeByte(bits[1])
        self._writeByte(bits[0])

    def _writeBytesP(self, n: int):
        if n <= 9:
            self._writeByte((0x30 + n).to_bytes(1, "big"))
        else :
            self._writeByte((0x30 + (n // 10)).to_bytes(1, "big"))
            self._writeByte((0x30 + (n % 10)).to_bytes(1, "big"))