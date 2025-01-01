"""
Accepted
130 [Medium]
Runtime: 4 ms, faster than 76.74% of Python3 online submissions for Surrounded Regions.
Memory Usage: 21.95 MB, less than 23.19% of Python3 online submissions for Surrounded Regions.
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        visited = set()
        def dfs(row, col):
            if row == -1 or row == M or col == -1 or col == N or board[row][col] == 'X' or (row, col) in visited:
                return

            visited.add((row, col))
            for dx, dy in directions:
                dfs(row + dx, col + dy)

        for row in range(M):
            dfs(row, 0)
            dfs(row, N - 1)
        for col in range(N):
            dfs(0, col)
            dfs(M - 1, col)

        for row in range(M):
            for col in range(N):
                if (row, col) not in visited:
                    board[row][col] = 'X'