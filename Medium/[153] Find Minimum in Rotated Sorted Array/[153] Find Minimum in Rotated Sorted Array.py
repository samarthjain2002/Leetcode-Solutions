"""
Accepted
153 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 17.80 MB, less than 6.78% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        left, right = 1, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid