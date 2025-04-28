"""
Accepted
2296 [Hard]
Runtime: 1946 ms, faster than 17.63% of Python3 online submissions for Design a Text Editor.
Memory Usage: 30.74 MB, less than 93.76% of Python3 online submissions for Design a Text Editor.
"""
class TextEditor:

    def __init__(self):
        self.string = ""
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.string = self.string[ : self.cursor] + text + self.string[self.cursor : ]
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        minimum = min(k, self.cursor)
        prevPos = self.cursor
        self.cursor -= minimum
        self.string = self.string[ : self.cursor] + self.string[prevPos : ]
        return minimum

    def cursorLeft(self, k: int) -> str:
        self.cursor -= min(k, self.cursor)
        minimum = min(10, len(self.string[ : self.cursor]))
        return self.string[self.cursor - minimum : self.cursor]

    def cursorRight(self, k: int) -> str:
        self.cursor += min(k, len(self.string[self.cursor : ]))
        minimum = min(10, len(self.string[ : self.cursor]))
        return self.string[self.cursor - minimum : self.cursor]


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)