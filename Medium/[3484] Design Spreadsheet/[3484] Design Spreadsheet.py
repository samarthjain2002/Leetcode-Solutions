"""
Accepted
3484 [Medium]
Runtime: 139 ms, faster than 53.98% of Python3 online submissions for Design Spreadsheet.
Memory Usage: 23.86 MB, less than 18.05% of Python3 online submissions for Design Spreadsheet.
"""
class Spreadsheet:
    def __init__(self, rows: int):
        self.spreadsheet = [[0] * rows for i in range(26)]        

    def setCell(self, cell: str, value: int) -> None:
        col = int(ord(cell[0])) - 65
        row = int(cell[1 : ]) - 1

        self.spreadsheet[col][row] = value

    def resetCell(self, cell: str) -> None:
        col = int(ord(cell[0])) - 65
        row = int(cell[1 : ]) - 1

        self.spreadsheet[col][row] = 0  

    def getValue(self, formula: str) -> int:
        cell1, cell2 = formula.split('+')
        if cell1[1] in string.ascii_letters:
            col = int(ord(cell1[1])) - 65
            row = int(cell1[2 : ]) - 1

            val1 = self.spreadsheet[col][row]
        else:
            val1 = int(cell1[1 : ])

        if cell2[0] in string.ascii_letters:
            col = int(ord(cell2[0])) - 65
            row = int(cell2[1 : ]) - 1

            val2 = self.spreadsheet[col][row]
        else:
            val2 = int(cell2[0 : ])
            
        return val1 + val2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)