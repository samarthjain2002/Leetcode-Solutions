"""
Accepted
91 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Decode Ways.
Memory Usage: 17.98 MB, less than 8.06% of Python3 online submissions for Decode Ways.
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if (i + 1 < len(s) and ((s[i] == '1') or (s[i] == '2' and s[i + 1] in "0123456"))):
                dp[i] += dp[i + 2]
        return dp[0]