"""
Accepted
300 [Medium]
Runtime: 1828 ms, faster than 63.96% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage:  17.84 MB, less than 8.61% of Python3 online submissions for Longest Increasing Subsequence.
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS_DP = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    LIS_DP[i] = max(LIS_DP[i], LIS_DP[j] + 1)

        return max(LIS_DP)