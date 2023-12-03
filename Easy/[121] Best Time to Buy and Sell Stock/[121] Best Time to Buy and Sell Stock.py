"""
Accepted
121 [Easy]
Runtime: 863 ms, faster than 56.38% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 27.18 MB, less than 93.66% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1

        return maxProfit