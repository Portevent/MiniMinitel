
from minitel.minitel import Minitel

class MinitelController(Minitel):

    def writeAt(self, x: int, y: int, text: str):
        self.cursorMoveTo(x, y);
        self.write(text)