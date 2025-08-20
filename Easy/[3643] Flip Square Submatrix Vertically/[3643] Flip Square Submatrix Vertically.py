"""
Accepted
3643 [Easy]
Runtime: 10 ms, faster than 5.00% of Python3 online submissions for Flip Square Submatrix Vertically.
Memory Usage: 18.02 MB, less than 51.52% of Python3 online submissions for Flip Square Submatrix Vertically.
"""
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        newGrid = [[0] * len(grid[0]) for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if x <= i < x + k and y <= j < y + k:
                    newGrid[i][j] = grid[(x + k - 1) - (i - x)][j]
                else:
                    newGrid[i][j] = grid[i][j]

        return newGrid