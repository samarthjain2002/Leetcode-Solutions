"""
Accepted
962 [Medium]
Runtime: 402 ms, faster than 17.02% of Python3 online submissions for Maximum Width Ramp.
Memory Usage:  23.74 MB, less than 40.43% of Python3 online submissions for Maximum Width Ramp.
"""
# Pre-processing approach
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maxRight = [0] * len(nums)
        maxNum = 0
        for i in range(len(nums) - 1, -1, -1):
            maxRight[i] = max(nums[i], maxNum)
            maxNum = maxRight[i]

        left = 0
        res = 0
        for right in range(len(nums)):
            while nums[left] > maxRight[right]:
                left += 1
            res = max(res, right - left)
        return res



# MonotonicStack approach
"""
Runtime: 356 ms, faster than 42.10% of Python3 online submissions for Maximum Width Ramp.
Memory Usage:  23.62 MB, less than 56.38% of Python3 online submissions for Maximum Width Ramp.
"""
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        monotonicStack = []
        for i, num in enumerate(nums):
            if not monotonicStack or nums[monotonicStack[-1]] > num:
                monotonicStack.append(i)

        res = 0
        for j in range(len(nums) - 1, -1, -1):
            while monotonicStack and nums[monotonicStack[-1]] <= nums[j]:
                res = max(res, j - monotonicStack.pop())
        return res