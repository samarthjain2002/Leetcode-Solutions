"""
Accepted
3356 [Medium]
Runtime: 1238 ms, faster than 22.40% of Python3 online submissions for Zero Array Transformation II.
Memory Usage: 144.67 MB, less than 30.47% of Python3 online submissions for Zero Array Transformation II.
"""
# Difference Array + Binary Search on Answer approach
# TC: O(log(q) * (q + n)), SC: O(n)
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if sum(nums) == 0:
            return 0

        low, high = 0, len(queries) - 1
        res = -1
        while low <= high:
            mid = low + ((high - low) // 2)

            # Build heights
            heights = [0] * len(nums)
            for i in range(mid + 1):
                left, right, val = queries[i]
                if left > 0:
                    heights[left - 1] -= val
                heights[right] += val

            # Set all heights correctly
            curHeight = 0
            for i in reversed(range(len(heights))):
                curHeight += heights[i]
                heights[i] = curHeight

            # Check if every element has enough height
            valid = True
            for i in range(len(nums)):
                # If height is not enough
                if nums[i] > heights[i]:
                    valid = False
                    break

            # If height is enough, the previous if condition isn't True
            if valid:
                # res = query index + 1 (query count)
                res = mid + 1
                high = mid - 1
            else:
                low = mid + 1

        return res