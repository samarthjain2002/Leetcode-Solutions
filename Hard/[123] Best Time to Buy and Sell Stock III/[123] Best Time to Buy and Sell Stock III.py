"""
Accepted
123 [Hard]
Runtime: 1952 ms, faster than 7.91% of Python3 online submissions for Best Time to Buy and Sell Stock III.
Memory Usage: 450.99 MB, less than 6.88% of Python3 online submissions for Best Time to Buy and Sell Stock III.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def rec(i, holding, count):
            if i == len(prices) or count == 2:
                return 0
            if (i, holding, count) in cache:
                return cache[(i, holding, count)]

            cooldown = rec(i + 1, holding, count)
            if holding:
                sell = rec(i + 1, False, count + 1) + prices[i]
                cache[(i, holding, count)] = max(sell, cooldown)
            else:
                buy = rec(i + 1, True, count) - prices[i]
                cache[(i, holding, count)] = max(buy, cooldown)
            
            return cache[(i, holding, count)]

        return rec(0, False, 0)