"""
Accepted
1351 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 18.47 MB, less than 88.21% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
"""
# TC: O(m + n), SC: O(1)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        x, y = 0, len(grid[0])
        res = 0
        while x < len(grid) and 0 <= y:
            if y == 0 or grid[x][y - 1] >= 0:
                res += len(grid[0]) - y
                x += 1
            else:
                y -= 1
        return res