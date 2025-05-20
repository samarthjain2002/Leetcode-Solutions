"""
Accepted
3355 [Medium]
Runtime: 63 ms, faster than 95.26% of Python3 online submissions for Zero Array Transformation I.
Memory Usage: 54.76 MB, less than 97.54% of Python3 online submissions for Zero Array Transformation I.
"""
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # Build heights
        heights = [0] * len(nums)
        for query in queries:
            left, right = query
            if left > 0:
                heights[left - 1] -= 1
            heights[right] += 1

        # Set all heights correctly
        curHeight = 0
        for i in reversed(range(len(heights))):
            curHeight += heights[i]
            heights[i] = curHeight

        # Check if every element has enough height
        for i in range(len(nums)):
            if nums[i] > heights[i]:
                return False
        return True