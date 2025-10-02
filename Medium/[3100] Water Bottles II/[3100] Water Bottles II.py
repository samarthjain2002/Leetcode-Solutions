"""
Accepted
3100 [Medium]
Runtime: 36 ms, faster than 75.00% of Python3 online submissions for Water Bottles II.
Memory Usage: 17.80 MB, less than 43.33% of Python3 online submissions for Water Bottles II.
"""
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        fullBottles = numBottles
        emptyBottles = 0
        bottlesDrunk = 0
        while fullBottles or emptyBottles:
            while emptyBottles >= numExchange:
                emptyBottles -= numExchange
                fullBottles += 1
                numExchange += 1
            if emptyBottles < numExchange and fullBottles == 0:
                break
            bottlesDrunk += fullBottles
            emptyBottles += fullBottles
            fullBottles = 0
        return bottlesDrunk