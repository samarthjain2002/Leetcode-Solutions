"""
Accepted
2028 [Medium]
Runtime: 1020 ms, faster than 34.49% of Python3 online submissions for Find Missing Observations.
Memory Usage: 27.37 MB, less than 32.89% of Python3 online submissions for Find Missing Observations.
"""
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)

        sumOfmDiceRolls = sum(rolls)
        sumOfnDiceRolls = ((m + n) * mean) - sumOfmDiceRolls
        
        if sumOfnDiceRolls / n > 6:
            return []
        if mean < (sumOfmDiceRolls + n) / (m + n):
            return []

        res = []
        for i in range(n, 0, -1):
            roll = sumOfnDiceRolls // i
            res.append(roll)
            sumOfnDiceRolls -= roll
        return res