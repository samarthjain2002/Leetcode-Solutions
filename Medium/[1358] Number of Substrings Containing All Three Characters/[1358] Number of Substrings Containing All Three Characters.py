"""
Accepted
1358 [Medium]
Runtime: 331 ms, faster than 10.28% of Python3 online submissions for Number of Substrings Containing All Three Characters.
Memory Usage: 18.12 MB, less than 17.65% of Python3 online submissions for Number of Substrings Containing All Three Characters.
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        
        charFreq = {char: 0 for char in "abc"}
        res = 0
        left = 0
        for right in range(len(s)):
            charFreq[s[right]] += 1
            while left <= right and all(freq for freq in charFreq.values()):
                res += N - right
                charFreq[s[left]] -= 1
                left += 1
        return res