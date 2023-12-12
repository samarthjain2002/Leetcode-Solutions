"""
Accepted
1464 [Easy]
Runtime: 57 ms, faster than 53.82% of Python3 online submissions for Maximum Product of Two Elements in an Array.
Memory Usage: 16.44 MB, less than 10.60% of Python3 online submissions for Maximum Product of Two Elements in an Array.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-2] - 1) * (nums[-1] - 1)