"""
Accepted
3 [Medium]
Runtime: 324 ms, faster than 9.76% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 16.57 MB, less than 94.31% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        N = len(s)
        for left in range(N):
            right = left + 1
            count = 1
            while right < N and s[right] not in s[left: right]:
                right += 1
                count += 1
            else:
                res = max(res, count)

        return res