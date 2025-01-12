"""
Accepted
63 [Medium]
Runtime: 4 ms, faster than 10.71% of Python3 online submissions for Unique Paths II.
Memory Usage: 17.83 MB, less than 31.87% of Python3 online submissions for Unique Paths II.
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        if obstacleGrid[-1][-1] == 0:
            dp[-1][-1] = 1
        
        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                if obstacleGrid[i][j] == 0:
                    if i == ROWS - 1 and j == COLS - 1:
                        pass
                    elif i == ROWS - 1:
                        dp[i][j] = dp[i][j + 1]
                    elif j == COLS - 1:
                        dp[i][j] = dp[i + 1][j]
                    else:
                        dp[i][j] = dp[i][j + 1] + dp[i + 1][j]
        return dp[0][0]