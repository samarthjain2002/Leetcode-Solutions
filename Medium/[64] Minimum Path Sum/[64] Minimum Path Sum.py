"""
Accepted
64 [Medium]
Runtime: 81 ms, faster than 5.30% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 28.29 MB, less than 8.93% of Python3 online submissions for Minimum Path Sum.
"""
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