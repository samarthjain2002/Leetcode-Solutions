"""
Accepted
1685 [Medium]
Runtime: 812 ms, faster than 8.92% of Python3 online submissions for Sum of Absolute Differences in a Sorted Array.
Memory Usage: 31.88 MB, less than 30.57% of Python3 online submissions for Sum of Absolute Differences in a Sorted Array.
"""
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        totalSum = sum(nums)
        left = 0
        right = totalSum - nums[0]
        res = []
        for i in range(0,len(nums)):
            val = (nums[i] * i) - left
            val += right - (nums[i] * (len(nums) - i - 1))
            res.append(val)
            left += nums[i]
            if i < len(nums) - 1:
                right = totalSum - left - nums[i + 1]
            else:
                right = 0

        return res