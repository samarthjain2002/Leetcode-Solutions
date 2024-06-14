"""
Accepted
945 [Medium]
Runtime: 663 ms, faster than 29.05% of Python3 online submissions for Minimum Increment to Make Array Unique.
Memory Usage: 30.30 MB, less than 79.28% of Python3 online submissions for Minimum Increment to Make Array Unique.
"""
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                res += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return res