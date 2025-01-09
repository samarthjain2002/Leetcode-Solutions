"""
Accepted
980 [Hard]
Runtime: 15 ms, faster than 52.35% of Python3 online submissions for Unique Paths III.
Memory Usage: 17.56 MB, less than 48.42% of Python3 online submissions for Unique Paths III.
"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        walkable = 1
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    walkable += 1
                elif grid[i][j] == 1:
                    start = [i, j]

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        visited = set()
        res = 0
        def dfs(i, j):
            nonlocal walkable, res
            if i in [-1, M] or j in [-1, N] or (i, j) in visited or grid[i][j] == -1:
                return

            if grid[i][j] == 2:
                if walkable == 0:
                    res += 1
                return

            walkable -= 1
            visited.add((i, j))

            for dx, dy in directions:
                dfs(i + dx, j + dy)

            walkable += 1
            visited.remove((i, j))

        dfs(start[0], start[1])
        return res