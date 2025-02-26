"""
Accepted
1749 [Medium]
Runtime: 106 ms, faster than 16.83% of Python3 online submissions for Maximum Absolute Sum of Any Subarray.
Memory Usage: 21.28 MB, less than 16.59% of Python3 online submissions for Maximum Absolute Sum of Any Subarray.
"""
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = 0
        def maxSum(nums):
            nonlocal res
            count = 0
            for num in nums:
                count += num
                count = max(count, 0)
                res = max(res, count)

        maxSum(nums)
        nums = [-num for num in nums]
        maxSum(nums)

        return res