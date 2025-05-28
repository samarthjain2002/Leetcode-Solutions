"""
Accepted
162 [Medium]
Runtime: 59 ms, faster than 36.27% of Python3 online submissions for Find Peak Element.
Memory Usage: 20.48 MB, less than 62.18% of Python3 online submissions for Find Peak Element.
"""
# Binary Search approach
# TC: O(logn), SC: O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if (mid == 0 or nums[mid - 1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                return mid
            elif mid == 0 or nums[mid + 1] > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1