"""
Accepted
1043 [Medium]
Runtime: 271 ms, faster than 94.78% of Python3 online submissions for Partition Array for Maximum Sum.
Memory Usage:  16.77 MB, less than 72.76% of Python3 online submissions for Partition Array for Maximum Sum.
"""
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        dp = [0] * N
        for i in range(0, len(arr)):
            m, d = -float("inf"), -float("inf")
            for j in range(0, min(k, i + 1)):
                m = max(m, arr[i - j])
                d = max(d, m * (j + 1) + dp[i - j - 1])
            dp[i] = d

        return dp[-1]