"""
Accepted
540 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Single Element in a Sorted Array.
Memory Usage: 24.88 MB, less than 45.95% of Python3 online submissions for Single Element in a Sorted Array.
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if (mid > 0 and nums[mid - 1] == nums[mid]) or (mid + 1 < len(nums) and nums[mid + 1] == nums[mid]):
                if mid + 1 < len(nums) and nums[mid + 1] == nums[mid]:
                    if (len(nums) - mid) % 2:
                        low = mid + 1
                    else:
                        high = mid - 1
                elif mid > 0 and nums[mid - 1] == nums[mid]:
                    if (len(nums) - mid) % 2:
                        high = mid - 1
                    else:
                        low = mid + 1
            else:
                return nums[mid]