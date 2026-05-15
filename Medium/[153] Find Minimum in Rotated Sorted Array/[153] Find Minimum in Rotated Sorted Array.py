"""
Accepted
153 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 19.38 MB, less than 66.55% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
"""
# Binary Search Solution
# TC: O(logn), SC: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Has not been rotated
        if nums[0] <= nums[-1]:
            return nums[0]

        low, high = 0, len(nums) - 1
        while low < high:   # Until low and high are equal
            mid = low + ((high - low) // 2)
            if nums[mid] < nums[high]:
                high = mid      # Mid could be the minimum element
            else:
                low = mid + 1   # mid is not the ans, so exclude it
        return nums[low]    # Low and high point to ans



"""
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