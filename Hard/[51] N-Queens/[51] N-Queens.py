"""
Accepted
51 [Hard]
Runtime: 63 ms, faster than 10.82% of Python3 online submissions for N-Queens.
Memory Usage: 18.92 MB, less than 8.51% of Python3 online submissions for N-Queens.
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        board = [[0] * n for _ in range(n)]
        
        def is_safe(row, col):
            for r in range(n):
                if board[r][col]:
                    return False

            # North-West
            for i in range(1, min(row, col) + 1):
                if board[row - i][col - i]:
                    return False

            # North-East
            for i in range(1, min(row, n - col - 1) + 1):
                if board[row - i][col + i]:
                    return False

            # South-West
            for i in range(1, min(n - row - 1, col) + 1):
                if board[row + i][col - i]:
                    return False

            # South-East
            for i in range(1, min(n - row - 1, n - col - 1) + 1):
                if board[row + i][col + i]:
                    return False

            return True

        def backtrack(row, col):
            if col == n:
                return False

            if row == n:
                solutions.append(copy.deepcopy(board))
                return

            if is_safe(row, col):
                board[row][col] = 1
                backtrack(row + 1, 0)
                board[row][col] = 0

            backtrack(row, col + 1)

                    
        backtrack(0, 0)

        for i, solution in enumerate(solutions):
            board = []
            for row in solution:
                string = ""
                for col in row:
                    if col:
                        string += 'Q'
                    else:
                        string += '.'
                board.append(string)
            solutions[i] = board

        return solutions