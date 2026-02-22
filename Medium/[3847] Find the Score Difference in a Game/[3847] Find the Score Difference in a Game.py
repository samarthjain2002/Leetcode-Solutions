"""
Accepted
3847 [Medium]
Runtime: 7 ms, faster than 90.32% of Python3 online submissions for Find the Score Difference in a Game.
Memory Usage: 19.43 MB less than 62.39% of Python3 online submissions for Find the Score Difference in a Game.
"""
class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        pl1 = pl2 = 0
        pl1Active = True
        for i, num in enumerate(nums):
            if num % 2 and (i + 1) % 6 == 0:
                pass
            elif num % 2 or (i + 1) % 6 == 0:
                pl1Active = not pl1Active

            if pl1Active:
                pl1 += num
            else:
                pl2 += num
                
        return pl1 - pl2