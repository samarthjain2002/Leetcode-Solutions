"""
Accepted
2441 [Easy]
Runtime: 97 ms, faster than 95.90% of Python3 online submissions for Largest Positive Integer That Exists With Its Negative.
Memory Usage: 16.69 MB, less than 98.70% of Python3 online submissions for Largest Positive Integer That Exists With Its Negative.
"""
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] < 0 and nums[right] > 0:
                if abs(nums[left]) == nums[right]:
                    return nums[right]
                elif abs(nums[left]) > nums[right]:
                    left += 1
                else:
                    right -= 1
            else:
                return -1
        return -1