"""
Accepted
790 [Medium]
Runtime: 1 ms, faster than 67.67% of Python3 online submissions for Domino and Tromino Tiling.
Memory Usage:  17.88 MB, less than 48.23% of Python3 online submissions for Domino and Tromino Tiling.
"""
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] * 2 + dp[i - 3]
        return dp[n] % (10**9 + 7)