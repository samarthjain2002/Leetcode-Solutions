"""
Accepted
2016 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Maximum Difference Between Increasing Elements.
Memory Usage: 17.81 MB, less than 59.91% of Python3 online submissions for Maximum Difference Between Increasing Elements.
"""
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        smallest = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < smallest:
                smallest = nums[i]
            elif nums[i] > smallest:
                res = max(res, nums[i] - smallest)
        return res