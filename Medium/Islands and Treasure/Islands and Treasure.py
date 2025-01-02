class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfs(row, col, dist):
            if (row in [-1, ROWS] or col in [-1, COLS] or
                 grid[row][col] == -1 or grid[row][col] < dist):
                return

            grid[row][col] = dist
            for dx, dy in directions:
                dfs(row + dx, col + dy, dist + 1)        

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    dfs(row, col, 0)