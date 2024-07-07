"""
Accepted
1518 [Easy]
Runtime: 45 ms, faster than 5.97% of Python3 online submissions for Water Bottles.
Memory Usage: 16.41 MB, less than 79.17% of Python3 online submissions for Water Bottles.
"""
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            renew = numBottles // numExchange
            res += renew
            numBottles = numBottles - (renew * numExchange) + renew
        return res