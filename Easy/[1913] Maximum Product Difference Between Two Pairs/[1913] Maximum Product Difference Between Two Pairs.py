"""
Accepted
1913 [Easy]
Runtime: 161 ms, faster than 32.72% of Python online submissions for Maximum Product Difference Between Two Pairs.
Memory Usage: 17.77 MB, less than 35.35% of Python online submissions for Maximum Product Difference Between Two Pairs.
"""
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return ((nums[-1]*nums[-2]) - (nums[0]*nums[1]))