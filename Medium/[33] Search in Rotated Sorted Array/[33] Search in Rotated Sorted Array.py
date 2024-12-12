"""
Accepted
33 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 17.83 MB, less than 5.25% of Python3 online submissions for Search in Rotated Sorted Array.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            
            # Left side is sorted
            if nums[left] <= nums[mid]:
                if target < nums[left]:
                    left = mid + 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            # Right side is sorted
            else:
                if target > nums[right]:
                    right = mid - 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                         
        return -1