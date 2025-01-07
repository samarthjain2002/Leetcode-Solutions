"""
Accepted
518 [Medium]
Runtime: 394 ms, faster than 38.90% of Python3 online submissions for Coin Change II.
Memory Usage: 48.25 MB, less than 45.03% of Python3 online submissions for Coin Change II.
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        # COLS: 0 to amount, ROWS: coins
        dp = [[0] * (amount + 1) for _ in range(N)]

        # I can make 0 amount without picking any coin, so 1 denomination
        for i in range(N):
            dp[i][0] = 1

        for i in range(N - 1, -1, -1):
            for a in range(1, amount + 1):
                # If I choose to pick the coin
                pick = a - coins[i]
                if pick >= 0:
                    dp[i][a] = dp[i][pick]
                # If I don't choose to pick the coin
                if i < N - 1:
                    dp[i][a] += dp[i + 1][a]
                # Add them both
                
        return dp[0][-1]