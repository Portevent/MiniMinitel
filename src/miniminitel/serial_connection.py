import serial

class SerialConnection:
    """
    Raw SerialConnection interface
    """

    def __init__(self, port: str = '/dev/ttyUSB0', baudrate=4800):
        self.ser = serial.Serial(port, baudrate=baudrate, bytesize=7, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ser.close()

    def _write_byte(self, byte: bytes):
        """
        Send byte over serial connection
        :param byte: Bytes to send
        """
        self.ser.write(byte)


    def _write_bytes_p(self, n: int):
        if n <= 9:
            self._write_byte((0x30 + n).to_bytes(1, "big"))
        else :
            self._write_byte((0x30 + (n // 10)).to_bytes(1, "big"))
            self._write_byte((0x30 + (n % 10)).to_bytes(1, "big"))