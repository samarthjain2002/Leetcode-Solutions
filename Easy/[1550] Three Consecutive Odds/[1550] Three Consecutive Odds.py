"""
Accepted
1550 [Easy]
Runtime: 41 ms, faster than 89.04% of Python3 online submissions for Three Consecutive Odds.
Memory Usage: 16.65 MB, less than 67.76% of Python3 online submissions for Three Consecutive Odds.
"""
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i, num in enumerate(arr):
            if num % 2 != 0:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return False