"""
Accepted
529 [Medium]
Runtime: 4 ms, faster than 78.67% of Python3 online submissions for Minesweeper.
Memory Usage:  20.34 MB, less than 5.63% of Python3 online submissions for Minesweeper.
"""
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        M, N = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or x >= M or y < 0 or y >= N or board[x][y] != 'E':
                return
            
            directions = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]

            mines = 0
            for dr, dc in directions:
                newRow, newCol = x + dr, y + dc            
                if 0 <= newRow < M and 0 <= newCol < N and board[newRow][newCol] == 'M':
                    mines += 1

            if mines:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for dr, dc in directions:
                    dfs(x + dr, y + dc)


        dfs(click[0], click[1])
        return board