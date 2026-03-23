"""
Accepted
1594 [Medium]
Runtime: 3 ms, faster than 85.09% of Python3 online submissions for Maximum Non Negative Product in a Matrix.
Memory Usage: 19.40 MB, less than 88.60% of Python3 online submissions for Maximum Non Negative Product in a Matrix.
"""
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and  j == 0:
                    maxi = mini = grid[i][j]
                elif i == 0:
                    maxi = max(grid[i][j - 1][0] * grid[i][j], grid[i][j - 1][1] * grid[i][j])
                    mini = min(grid[i][j - 1][0] * grid[i][j], grid[i][j - 1][1] * grid[i][j])
                elif j == 0:
                    maxi = max(grid[i - 1][j][0] * grid[i][j], grid[i - 1][j][1] * grid[i][j])
                    mini = min(grid[i - 1][j][0] * grid[i][j], grid[i - 1][j][1] * grid[i][j])
                else:
                    maxi = max(
                        grid[i - 1][j][0] * grid[i][j], grid[i - 1][j][1] * grid[i][j],
                        grid[i][j - 1][0] * grid[i][j], grid[i][j - 1][1] * grid[i][j]
                    )
                    mini = min(
                        grid[i - 1][j][0] * grid[i][j], grid[i - 1][j][1] * grid[i][j],
                        grid[i][j - 1][0] * grid[i][j], grid[i][j - 1][1] * grid[i][j]
                    )
                
                grid[i][j] = [maxi, mini]

        if grid[i][j][0] >= 0:
            return grid[i][j][0] % MOD
        else:
            return -1