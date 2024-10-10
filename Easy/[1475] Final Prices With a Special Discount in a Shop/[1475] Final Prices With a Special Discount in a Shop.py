"""
Accepted
1475 [Easy]
Runtime: 49 ms, faster than 55.65% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
Memory Usage:  16.53 MB, less than 80.35% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
"""
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        monotonicStack = []
        for i, num in enumerate(prices):
            while monotonicStack and prices[monotonicStack[-1]] >= num:
                index = monotonicStack.pop()
                prices[index] -= num
            monotonicStack.append(i)
        return prices