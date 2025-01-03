"""
Accepted
300 [Medium]
Runtime: 7 ms, faster than 85.94% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage:  18.07 MB, less than 19.42% of Python3 online submissions for Longest Increasing Subsequence.
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



"""
Runtime: 1794 ms, faster than 48.07% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage:  18.25 MB, less than 10.80% of Python3 online submissions for Longest Increasing Subsequence.
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)

        dp = [1] * N
        for i in range(N - 2, -1, -1):
            for j in range(i + 1, N):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)