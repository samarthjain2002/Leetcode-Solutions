"""
Accepted
1020 [Medium]
Runtime: 395 ms, faster than 5.07% of Python3 online submissions for Number of Enclaves.
Memory Usage: 54.78 MB, less than 9.94% of Python3 online submissions for Number of Enclaves.
"""
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        boundaryIsland = {}
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        islandCells = {}
        def dfs(row, col, ID):
            if row in [-1, len(grid)] or col in [-1, len(grid[0])]:
                boundaryIsland[ID] = True
                return
            if (row, col) in visited or grid[row][col] == 0:
                return

            visited.add((row, col))
            islandCells[ID] += 1
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                dfs(nr, nc, ID)

        
        islandCount = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    islandCount += 1
                    islandCells[islandCount] = 0
                    boundaryIsland[islandCount] = False
                    dfs(i, j, islandCount)
        
        res = 0
        for ID, bIsland in boundaryIsland.items():
            if not bIsland:
                res += islandCells[ID]
        return res