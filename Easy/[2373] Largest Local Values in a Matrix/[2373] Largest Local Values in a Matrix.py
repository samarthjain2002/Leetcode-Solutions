"""
Accepted
2373 [Easy]
Runtime: 133 ms, faster than 47.35% of Java online submissions for Largest Local Values in a Matrix.
Memory Usage: 17.17 MB, less than 28.98% of Java online submissions for Largest Local Values in a Matrix.
"""
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(grid) - 2):
            res.append([])
            for j in range(len(grid[0]) - 2):
                m = -1
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        m = max(m, grid[row][col])
                res[-1].append(m)
        return res