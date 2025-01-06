"""
Accepted
309 [Medium]
Runtime: 8 ms, faster than 24.69% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
Memory Usage:  18.07 MB, less than 19.42% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = {}

        def rec(i, buying):
            if i >= N:
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                buy = rec(i + 1, False) - prices[i]
                cooldown = rec(i + 1, True)
                dp[(i, True)] = max(buy, cooldown)
            else:
                sell = rec(i + 2, True) + prices[i]
                cooldown = rec(i + 1, False)
                dp[(i, False)] = max(sell, cooldown)
            return dp[(i, buying)]

        return rec(0, True)