"""
Accepted
154 [Hard]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
Memory Usage: 19.52 MB, less than 55.91% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
"""
# Binary Search Solution
# TC: Best Ω(log n), Average Θ(log n), Worst O(n), SC: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + ((high - low) // 2)
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high -= 1
        return nums[low]