"""
Accepted
1509 [Medium]
Runtime: 276 ms, faster than 64.62% of Python online submissions for Minimum Difference Between Largest and Smallest Value in Three Moves.
Memory Usage: 27.43 MB, less than 39.86% of Python online submissions for Minimum Difference Between Largest and Smallest Value in Three Moves.
"""
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 4:
            return 0
            
        nums.sort()
        res = float("inf")
        for i in range(4):
            res = min(res, nums[N - 4 + i] - nums[i])
        return res