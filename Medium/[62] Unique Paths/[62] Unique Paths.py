"""
Accepted
62 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Unique Paths.
Memory Usage: 17.98 MB, less than 7.28% of Python3 online submissions for Unique Paths.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row + 1 >= m and col + 1 >= n:
                    dp[row][col] = 1
                elif row + 1 >= m:
                    dp[row][col] = dp[row][col + 1] + 0
                elif col + 1 >= n:
                    dp[row][col] = dp[row + 1][col] + 0
                else:
                    dp[row][col] = dp[row][col + 1] + dp[row + 1][col]
        return dp[0][0]