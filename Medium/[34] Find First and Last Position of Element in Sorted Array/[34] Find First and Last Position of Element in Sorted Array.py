"""
Accepted
34 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 18.94 MB, less than 70.35% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + ((high - low) // 2)
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low if low < len(nums) and nums[low] == target else -1

        def findLast():
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + ((high - low) // 2)
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return high if high >= 0 and nums[high] == target else -1

        return [findFirst(), findLast()]