from src.mini_minitel.minitel_csi import MinitelCSI

class MinitelController(MinitelCSI):

    def write(self, text: str):
        self._writeByte(bytes(text, encoding="ascii"))

    def writeAt(self, x: int, y: int, text: str):
        self.cursorMoveTo(x, y)
        self.write(text)