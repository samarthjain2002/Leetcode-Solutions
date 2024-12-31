"""
Accepted
52 [Hard]
Runtime: 47 ms, faster than 12.21% of Python3 online submissions for N-Queens II.
Memory Usage: 17.89 MB, less than 12.76% of Python3 online submissions for N-Queens II.
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0] * n for _ in range(n)]
        res = 0

        def isSafe(row, col):
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
            nonlocal res
            if row == n:
                res += 1
                return

            if col == n:
                return

            if isSafe(row, col):
                board[row][col] = 1
                backtrack(row + 1, 0)
                board[row][col] = 0
            backtrack(row, col + 1)

        backtrack(0, 0)
        return res