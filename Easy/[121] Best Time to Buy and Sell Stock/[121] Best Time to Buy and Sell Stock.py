"""
Accepted
121 [Easy]
Runtime: 863 ms, faster than 56.38% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 27.18 MB, less than 93.66% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
# Greedy solution
# TC: O(n), SC: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        maxProfit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit



"""
Runtime: 189 ms, faster than 5.13% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 37.19 MB, less than 8.25% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
# HashMap solution
# TC: O(n), SC: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMaxPrice = prices[-1]
        max_future_price_at_i = {}
        for i in reversed(range(len(prices))):
            curMaxPrice = max(curMaxPrice, prices[i])
            max_future_price_at_i[i] = curMaxPrice

        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, max_future_price_at_i[i] - prices[i])
        return max(maxProfit, 0)



"""
Runtime: 863 ms, faster than 56.38% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 27.18 MB, less than 93.66% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
# TC: O(n), SC: O(1)
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