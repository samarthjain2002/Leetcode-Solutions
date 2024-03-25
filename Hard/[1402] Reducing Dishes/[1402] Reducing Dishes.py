"""
Accepted
1402 [Hard]
Runtime: 35 ms, faster than 96.57% of Python3 online submissions for Reducing Dishes.
Memory Usage: 16.53 MB, less than 80.60% of Python3 online submissions for Reducing Dishes.
"""
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        N = len(satisfaction)
        satisfaction.sort()
        prefixSum = sum(satisfaction)
        flag = False
        time = 1
        res = 0
        for i in range(N):
            if flag == False:
                if prefixSum >= 0:
                    flag = True
                else:
                    prefixSum -= satisfaction[i]
            if flag:
                res += satisfaction[i] * time
                time += 1

        return res