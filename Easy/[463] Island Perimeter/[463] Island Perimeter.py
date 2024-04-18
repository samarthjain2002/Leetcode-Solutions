"""
Accepted
463 [Easy]
Runtime: 357 ms, faster than 78.24% of Python3 online submissions for Island Perimeter.
Memory Usage: 16.94 MB, less than 65.66% of Python3 online submissions for Island Perimeter.
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        res = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    res += 4
                    if i != 0 and grid[i - 1][j] == 1:
                        res -= 2
                    if j != 0 and grid[i][j - 1] == 1:
                        res -= 2
        return res