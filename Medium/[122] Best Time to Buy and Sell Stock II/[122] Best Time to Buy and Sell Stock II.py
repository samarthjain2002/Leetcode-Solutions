"""
Accepted
122 [Medium]
Runtime: 57 ms, faster than 84.55% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage:  18.67 MB, less than 14.48% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        finProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                finProfit += profit
            left += 1
            right += 1

        return finProfit