"""
Accepted
64 [Medium]
Runtime: 19 ms, faster than 37.19% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 20.61 MB, less than 24.43% of Python3 online submissions for Minimum Path Sum.
"""
# Bottom-Up Tabulation approach
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    dp[i][j] = grid[i][j]
                elif i == len(grid) - 1:
                    dp[i][j] = dp[i][j + 1] + grid[i][j]
                elif j == len(grid[0]) - 1:
                    dp[i][j] = dp[i + 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]
        return dp[0][0]



"""
Runtime: 81 ms, faster than 5.30% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 28.29 MB, less than 8.93% of Python3 online submissions for Minimum Path Sum.
"""
# Top-Down Memoization approach
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = {}

        def dfs(i, j):
            if i in [-1, len(grid)] or j in [-1, len(grid[0])]:
                return float("inf")
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
                
            if (i, j) in cache:
                return cache[(i, j)]

            cache[(i, j)] = grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))
            return cache[(i, j)]


        return dfs(0, 0)