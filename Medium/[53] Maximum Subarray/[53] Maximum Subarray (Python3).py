"""
Accepted
53 [Medium]
Runtime: 622 ms, faster than 36.16% of Python3 online submissions for Maximum Subarray.
Memory Usage: 29.13 MB, less than 92.01% of Python3 online submissions for Maximum Subarray.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -10001
        curSum = -10001

        for i in nums:
            curSum = max(curSum+i, i)
            maxSum = max(maxSum, curSum)
            
        return maxSum



"""
Runtime: 77 ms, faster than 47.50% of Python3 online submissions for Maximum Subarray.
Memory Usage: 32.89 MB, less than 23.40% of Python3 online submissions for Maximum Subarray.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
            
        res = float("-inf")
        count = 0
        startIndex = 0
        for i in range(len(nums)):
            count += nums[i % len(nums)]
            if count < 0:
                count = 0
                startIndex = i + 1
                continue

            if i - startIndex < len(nums):
                res = max(res, count)

        return res