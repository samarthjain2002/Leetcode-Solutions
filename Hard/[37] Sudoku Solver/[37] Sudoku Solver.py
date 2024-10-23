"""
Accepted
37 [Hard]
Runtime: 164 ms, faster than 65.56% of Python3 online submissions for Sudoku Solver.
Memory Usage:  16.77 MB, less than 28.84% of Python3 online submissions for Sudoku Solver.
"""
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        # Populating the hashSets for original board
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squareIndex = (i // 3) * 3 + (j // 3)
                    squares[squareIndex].add(board[i][j])
        
        def possible(i, j, num):
            squareIndex = (i // 3) * 3 + (j // 3)
            if num not in rows[i] and num not in cols[j] and num not in squares[squareIndex]:
                return True
            else:
                return False

        def placeNumber(i, j, num):
            board[i][j] = num
            rows[i].add(num)
            cols[j].add(num)
            squareIndex = (i // 3) * 3 + (j // 3)
            squares[squareIndex].add(num)

        def removeNumber(i, j, num):
            board[i][j] = '.'
            rows[i].remove(num)
            cols[j].remove(num)
            squareIndex = (i // 3) * 3 + (j // 3)
            squares[squareIndex].remove(num)

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if possible(i, j, num):
                                placeNumber(i, j, num)
                                if backtrack():
                                    return True
                                removeNumber(i, j, num)
                        return False
            return True

        backtrack()