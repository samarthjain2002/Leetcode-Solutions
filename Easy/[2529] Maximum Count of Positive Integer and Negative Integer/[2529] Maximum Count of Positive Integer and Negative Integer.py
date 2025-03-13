"""
Accepted
2529 [Easy]
Runtime: 0 ms, faster than 100.00% of Python online submissions for Maximum Count of Positive Integer and Negative Integer.
Memory Usage: 18.02 MB, less than 41.65% of Python online submissions for Maximum Count of Positive Integer and Negative Integer.
"""
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Returns the position of last negative element
        def lastNegEle():
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + ((high - low) // 2)
                if nums[mid] <= -1:
                    low = mid + 1
                else:
                    high = mid - 1
            return high

        # Returns the position of first positive element
        def firstPosEle():
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + ((high - low) // 2)
                if nums[mid] < 1:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        return max(lastNegEle() + 1, len(nums) - firstPosEle())