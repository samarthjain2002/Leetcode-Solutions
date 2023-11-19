"""
Accepted
53 [Medium]
Runtime: 548 ms, faster than 36.16% of Python online submissions for Maximum Subarray.
Memory Usage: 26.12 MB, less than 75.36% of Python online submissions for Maximum Subarray.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSum = -10001
        curSum = -10001

        for i in nums:
            curSum = max(curSum+i, i)
            maxSum = max(maxSum, curSum)
            
        return maxSum