"""
Accepted
2294 [Medium]
Runtime: 75 ms, faster than 92.99% of Python3 online submissions for Partition Array Such That Maximum Difference Is K.
Memory Usage: 29.04 MB, less than 73.61% of Python3 online submissions for Partition Array Such That Maximum Difference Is K.
"""
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        curMin = nums[0]
        res = 1
        for i in range(1, len(nums)):
            if nums[i] - curMin > k:
                res += 1
                curMin = nums[i]
        return res