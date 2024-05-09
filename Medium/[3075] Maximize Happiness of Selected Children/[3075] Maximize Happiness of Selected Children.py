"""
Accepted
3075 [Medium]
Runtime: 789 ms, faster than 79.39% of Python3 online submissions for Maximize Happiness of Selected Children.
Memory Usage: 43.54 MB, less than 33.89% of Python3 online submissions for Maximize Happiness of Selected Children.
"""
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        happiness.reverse()
        count = 0
        result = 0
        for i in range(len(happiness)):
            happiness[i] -= count
            count += 1
            if happiness[i] > 0 and k > 0:
                result += happiness[i]
                k -= 1
            else:
                return result
        return result