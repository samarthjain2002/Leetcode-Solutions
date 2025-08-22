"""
Accepted
3195 [Medium]
Runtime: 2626 ms, faster than 90.65% of Python3 online submissions for Find the Minimum Area to Cover All Ones I.
Memory Usage: 47.24 MB, less than 97.84% of Python3 online submissions for Find the Minimum Area to Cover All Ones I.
"""
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # top
        for i in range(m):
            if 1 in grid[i]:
                top = i
                break

        # bottom
        for i in range(m - 1, -1, -1):
            if 1 in grid[i]:
                bottom = i
                break

        # left
        for j in range(n):
            if any(grid[i][j] for i in range(m)):
                left = j
                break

        # right
        for j in range(n - 1, -1, -1):
            if any(grid[i][j] for i in range(m)):
                right = j
                break

        return (right - left + 1) * (bottom - top + 1)



"""
Runtime: 2955 ms, faster than 49.54% of Python3 online submissions for Find the Minimum Area to Cover All Ones I.
Memory Usage: 47.98 MB, less than 17.27% of Python3 online submissions for Find the Minimum Area to Cover All Ones I.
"""
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top, bottom = len(grid), 0
        left, right = len(grid[0]), 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)

        return (right - left + 1) * (bottom - top + 1)