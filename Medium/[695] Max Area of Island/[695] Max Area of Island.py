"""
Accepted
695 [Medium]
Runtime: 99 ms, faster than 87.58% of Python3 online submissions for Max Area of Island.
Memory Usage:  19.99 MB, less than 5.79% of Python3 online submissions for Max Area of Island.
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        visited = set()
        res = 0

        def dfs(i, j):
            if (i, j) in visited or i == -1 or i == M or j == -1 or j == N or grid[i][j] == 0:
                return 0
            visited.add((i, j))
            return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            
        for i in range(M):
            for j in range(N):
                if grid[i][j] and (i, j) not in visited:
                    islandSize = dfs(i, j)
                    res = max(res, islandSize)

        return res