"""
Accepted
494 [Medium]
Runtime: 191 ms, faster than 30.81% of Python3 online submissions for Target Sum.
Memory Usage: 38.50 MB, less than 27.86% of Python3 online submissions for Target Sum.
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = {}

        def rec(i, amount):
            if i >= N:
                if amount == target:
                    return 1
                else:
                    return 0
            if (i, amount) in dp:
                return dp[(i, amount)]

            dp[(i, amount)] = rec(i + 1, amount + nums[i]) + rec(i + 1, amount - nums[i])
            return dp[(i, amount)]

        return rec(0, 0)