from minitel.minitel_commands import MinitelCommands

class MinitelController(MinitelCommands):

    def writeAt(self, x: int, y: int, text: str):
        self.cursorMoveTo(x, y)
        self.write(text)