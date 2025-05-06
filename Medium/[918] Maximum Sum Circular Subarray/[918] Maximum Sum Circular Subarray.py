"""
Accepted
918 [Medium]
Runtime: 96 ms, faster than 66.73% of Python3 online submissions for Maximum Sum Circular Subarray.
Memory Usage: 21.37 MB, less than 53.56% of Python3 online submissions for Maximum Sum Circular Subarray.
"""
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax, globalMax = 0, nums[0]
        curMin, globalMin = 0, nums[0]
        totalSum = 0
        for num in nums:
            curMax = max(curMax + num, num)
            globalMax = max(globalMax, curMax)

            curMin = min(curMin + num, num)
            globalMin = min(globalMin, curMin)

            totalSum += num

        if totalSum == globalMin or globalMax > totalSum - globalMin:
            return globalMax
        else:
            return totalSum - globalMin