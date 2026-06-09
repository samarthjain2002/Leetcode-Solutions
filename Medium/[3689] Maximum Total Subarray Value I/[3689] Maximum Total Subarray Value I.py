"""
Accepted
3689 [Medium]
Runtime: 10 ms, faster than 73.60% of Python3 online submissions for Maximum Total Subarray Value I.
Memory Usage: 26.41 MB, less than 60.00% of Python3 online submissions for Maximum Total Subarray Value I.
"""
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums) - min(nums)) * k