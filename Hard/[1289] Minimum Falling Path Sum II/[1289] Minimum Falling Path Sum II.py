"""
Accepted
42 [Hard]
Runtime: 642 ms, faster than 51.01% of Java online submissions for Minimum Falling Path Sum II.
Memory Usage: 20.16 MB, less than 79.35% of Java online submissions for Minimum Falling Path Sum II.
"""
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        if N == 1:
            return grid[0][0]
        
        for row in range(1, N):
            for col in range(0, N):
                if col == 0:
                    grid[row][col] = min(grid[row - 1][1 : N]) + grid[row][col]
                elif col == N - 1:
                    grid[row][col] = min(grid[row - 1][0 : N - 1]) + grid[row][col]
                else:
                    grid[row][col] = min(min(grid[row - 1][0 : col]), min(grid[row - 1][col + 1 : N])) + grid[row][col]
                
        return min(grid[-1])