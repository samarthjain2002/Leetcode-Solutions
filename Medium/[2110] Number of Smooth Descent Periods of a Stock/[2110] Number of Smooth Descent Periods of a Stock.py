"""
Accepted
2110 [Medium]
Runtime: 51 ms, faster than 84.33% of Python3 online submissions for Number of Smooth Descent Periods of a Stock.
Memory Usage: 29.94 MB, less than 47.02% of Python3 online submissions for Number of Smooth Descent Periods of a Stock.
"""
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        left = 0
        res = 0
        for right in range(len(prices)):
            if left < right and prices[right - 1] != prices[right] + 1:
                n = right - left
                res += (n * (n + 1)) // 2
                left = right
        n = len(prices) - left
        return res + ((n * (n + 1)) // 2)