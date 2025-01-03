"""
Accepted
139 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Word Break.
Memory Usage:  17.79 MB, less than 26.14% of Python3 online submissions for Word Break.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)

        dp = [False] * (N + 1)
        dp[N] = True
        for i in range(N - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]