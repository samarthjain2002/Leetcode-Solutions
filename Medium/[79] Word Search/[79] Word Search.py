"""
Accepted
79 [Medium]
Runtime: 4528 ms, faster than 40.68% of Python3 online submissions for Word Search.
Memory Usage:  18.15 MB, less than 5.98% of Python3 online submissions for Word Search.
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, i):
            if i == len(word):
                return True

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[i]:
                return False            

            temp = board[row][col]
            board[row][col] = '#'

            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for dx, dy in directions:
                if backtrack(row + dx, col + dy, i + 1):
                    return True

            board[row][col] = temp
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, 0):
                    return True
        return False