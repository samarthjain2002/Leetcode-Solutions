"""
Accepted
1752 [Easy]
Runtime: 38 ms, faster than 57.97% of Python online submissions for Check if Array Is Sorted and Rotated.
Memory Usage: 17.64 MB, less than 70.45% of Python online submissions for Check if Array Is Sorted and Rotated.
"""
class Solution:
    def check(self, nums: List[int]) -> bool:
        j = len(nums)
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                j = i + 1
                break

        if j == len(nums) - 1 and nums[j] > nums[0]:
            return False
                
        for i in range(j, len(nums) - 1):
            if nums[i] > nums[i + 1] or nums[i] > nums[0] or nums[i + 1] > nums[0]:
                return False

        return True