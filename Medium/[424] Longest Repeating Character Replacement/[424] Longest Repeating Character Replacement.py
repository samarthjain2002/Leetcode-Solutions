"""
Accepted
424 [Medium]
Runtime: 114 ms, faster than 38.24% of Python3 online submissions for Longest Repeating Character Replacement.
Memory Usage:  17.54 MB, less than 19.03% of Python3 online submissions for Longest Repeating Character Replacement.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)

        freq = defaultdict(int)
        left = res = 0
        maxFreq = 0
        for right in range(N):
            freq[s[right]] += 1
            maxFreq = max(maxFreq, freq[s[right]])
            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res