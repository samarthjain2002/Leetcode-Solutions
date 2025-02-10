"""
Accepted
827 [Hard]
Runtime: 1783 ms, faster than 8.38% of Python3 online submissions for Making A Large Island.
Memory Usage: 16.62 MB, less than 28.74% of Python3 online submissions for Making A Large Island.
"""
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ID = 2
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        visited = set()
        def dfs(r, c):
            if r in [-1, len(grid)] or c in [-1, len(grid[0])] or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            grid[r][c] = ID
            visited.add((r, c))
            
            return 1 + sum(dfs(r + dr, c + dc) for (dr, dc) in directions)

        islandSize = {}
        biggestIsland = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = dfs(i, j)
                    islandSize[ID] = island
                    biggestIsland = max(biggestIsland, island)
                    ID += 1

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    count = 0
                    neiIslands = set()
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if (nx not in [-1, len(grid)] and ny not in [-1, len(grid[0])]
                             and grid[nx][ny] != 0):
                            neiIslands.add(grid[nx][ny])

                    count += sum(islandSize[ID] for ID in neiIslands)
                    res = max(res, count)

        return max(biggestIsland, res + 1)