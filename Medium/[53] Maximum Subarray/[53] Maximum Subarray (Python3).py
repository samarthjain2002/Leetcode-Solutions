"""
Accepted
53 [Medium]
Runtime: 622 ms, faster than 36.16% of Java online submissions for Maximum Subarray.
Memory Usage: 29.13 MB, less than 92.01% of Java online submissions for Maximum Subarray.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -10001
        curSum = -10001

        for i in nums:
            curSum = max(curSum+i, i)
            maxSum = max(maxSum, curSum)
            
        return maxSum