"""
Accepted
338 [Medium]
Runtime: 3 ms, faster than 94.98% of Python3 online submissions for Counting Bits.
Memory Usage: 18.39 MB, less than 55.85% of Python3 online submissions for Counting Bits.
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if i == offset * 2:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp