"""
Accepted
368 [Medium]
Runtime: 227 ms, faster than 52.07% of Python3 online submissions for Largest Divisible Subset.
Memory Usage:  16.90 MB, less than 76.96% of Python3 online submissions for Largest Divisible Subset.
"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[num] for num in nums]
        
        N = len(nums)
        res = []
        for i in range(N):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j] + [nums[i]]) > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]

            if len(res) < len(dp[i]):
                res = dp[i]

        return res