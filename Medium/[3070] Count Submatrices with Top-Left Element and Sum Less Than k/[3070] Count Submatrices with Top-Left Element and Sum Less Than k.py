"""
Accepted
3070 [Medium]
Runtime: 334 ms, faster than 51.61% of Python3 online submissions for Count Submatrices with Top-Left Element and Sum Less Than k.
Memory Usage: 64.82 MB, less than 85.81% of Python3 online submissions for Count Submatrices with Top-Left Element and Sum Less Than k.
"""
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] <= k:
                    res += 1
                else:
                    break
        return res