"""
Accepted
2460 [Easy]
Runtime: 4 ms, faster than 16.93% of Python3 online submissions for Apply Operations to an Array.
Memory Usage: 17.85 MB, less than 74.68% of Python3 online submissions for Apply Operations to an Array.
"""
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
            
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = 0, nums[right]
                left += 1

        return nums