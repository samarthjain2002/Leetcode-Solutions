"""
Accepted
2300 [Easy]
Runtime: 1156 ms, faster than 60.44% of Python3 online submissions for Successful Pairs of Spells and Potions.
Memory Usage: 40.11 MB, less than 13.93% of Python3 online submissions for Successful Pairs of Spells and Potions.
"""
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        N = len(potions)
        potions.sort()
        res = []
        for spell in spells:
            left, right = 0, N
            while left < right:
                mid = (left + right) // 2
                if spell * potions[mid] < success:
                    left = mid + 1
                else:
                    right = mid
            res.append(N - left)
        return res