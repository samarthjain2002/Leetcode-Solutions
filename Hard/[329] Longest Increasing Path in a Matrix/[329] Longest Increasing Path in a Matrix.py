"""
Accepted
329 [Hard]
Runtime: 289 ms, faster than 80.79% of Python3 online submissions for Longest Increasing Path in a Matrix.
Memory Usage: 17.60 MB, less than 92.34% of Python3 online submissions for Longest Increasing Path in a Matrix.
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[-1] * COLS for _ in range(ROWS)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            max_length = 1

            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < ROWS and 0 <= nj < COLS and matrix[ni][nj] > matrix[i][j]:
                    max_length = max(max_length, 1 + dfs(ni, nj))
            dp[i][j] = max_length

            return dp[i][j]
        
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                res = max(res, dfs(row, col))
        return res