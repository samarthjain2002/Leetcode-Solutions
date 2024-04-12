"""
Accepted
62 [Medium]
Runtime: 38 ms, faster than 40.69% of Python3 online submissions for Unique Paths.
Memory Usage: 16.59 MB, less than 41.63% of Python3 online submissions for Unique Paths.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j -1]
        return dp[m - 1][n - 1]