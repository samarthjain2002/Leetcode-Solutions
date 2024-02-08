"""
Accepted
279 [Medium]
Runtime: 2513 ms, faster than 55.73% of Python3 online submissions for Perfect Squares.
Memory Usage:  16.66 MB, less than 81.54% of Python3 online submissions for Perfect Squares.
"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target < square:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]