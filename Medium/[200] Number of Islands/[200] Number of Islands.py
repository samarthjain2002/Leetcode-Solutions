"""
Accepted
200 [Medium]
Runtime: 247 ms, faster than 53.59% of Python3 online submissions for Number of Islands.
Memory Usage:  27.78 MB, less than 9.47% of Python3 online submissions for Number of Islands.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])

        visited = set()
        res = 0

        def dfs(i, j):
            if (i, j) in visited or i == -1 or i == M or j == -1 or j == N or grid[i][j] == '0':
                return
            visited.add((i, j))
            dfs(i - 1, j)   # Top
            dfs(i, j + 1)   # Right
            dfs(i + 1, j)   # Bottom
            dfs(i, j - 1)   # Left

        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1' and (i, j) not in visited:
                    res += 1
                    dfs(i, j)
        
        return res