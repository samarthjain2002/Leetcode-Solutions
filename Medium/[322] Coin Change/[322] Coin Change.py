"""
Accepted
322 [Medium]
Runtime: 774 ms, faster than 56.60% of Python3 online submissions for Coin Change.
Memory Usage:  17.74 MB, less than 55.60% of Python3 online submissions for Coin Change.
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != float("inf") else -1