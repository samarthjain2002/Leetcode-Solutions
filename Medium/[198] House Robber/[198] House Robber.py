"""
Accepted
198 [Medium]
Runtime: 30 ms, faster than 94.79% of Python3 online submissions for House Robber.
Memory Usage:  16.66 MB, less than 56.34% of Python3 online submissions for House Robber.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1:
            return nums[0]
        elif N == 2:
            return max(nums)
        elif N == 3:
            return max(nums[0] + nums[2], nums[1])
        else:
            nums[2] += nums[0]

        for i in range(3, N):
            nums[i] += max(nums[i - 2], nums[i - 3])

        return max(nums[-1], nums[-2])