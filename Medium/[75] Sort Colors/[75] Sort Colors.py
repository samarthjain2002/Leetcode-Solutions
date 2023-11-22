"""
Accepted
75 [Medium]
Runtime: 49 ms, faster than 8.99% of Python3 online submissions for Sort Colors.
Memory Usage:  16.32 MB, less than 21.85% of Python3 online submissions for Sort Colors.
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j] < nums[i]:
                    nums[i] += nums[j]
                    nums[j] = nums[i] - nums[j]
                    nums[i] = nums[i] - nums[j]