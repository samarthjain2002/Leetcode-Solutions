"""
Accepted
1877 [Medium]
Runtime: 877 ms, faster than 67.63% of Python3 online submissions for Minimize Maximum Pair Sum in Array.
Memory Usage: 33.61 MB, less than 16.10% of Python3 online submissions for Minimize Maximum Pair Sum in Array.
"""
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        res = float("-inf")
        for i in range(len(nums) // 2):
            res = max(res, nums[i] + nums[N - (i + 1)])
        return res