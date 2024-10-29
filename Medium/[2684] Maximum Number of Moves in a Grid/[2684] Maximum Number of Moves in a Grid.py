"""
Accepted
2684 [Medium]
Runtime: 131 ms, faster than 63.64% of Python3 online submissions for Maximum Number of Moves in a Grid.
Memory Usage: 42.10 MB, less than 5.30% of Python3 online submissions for Maximum Number of Moves in a Grid.
"""
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        memo = {}

        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]

            res = 0
            if row > 0 and col < N - 1 and grid[row - 1][col + 1] > grid[row][col]:
                res = max(res, 1 + dfs(row - 1, col + 1))
            if col < N - 1 and grid[row][col + 1] > grid[row][col]:
                res = max(res, 1 + dfs(row, col + 1))
            if row < M - 1 and col < N - 1 and grid[row + 1][col + 1] > grid[row][col]:
                res = max(res, 1 + dfs(row + 1, col + 1))

            memo[(row, col)] = res

            return res

        res = 0
        for row in range(M):
            res = max(res, dfs(row, 0))
        return res