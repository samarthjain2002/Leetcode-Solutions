"""
Accepted
5 [Medium]
Runtime: 312 ms, faster than 54.93% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 17.72 MB, less than 33.71% of Python3 online submissions for Longest Palindromic Substring.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        resLeft, resRight = 1, -1
        for i in range(len(s)):
            # Odd length
            left = right = i
            while left >= 0 and right < N and s[left] == s[right]:
                if right - left + 1 > resRight - resLeft + 1:
                    resLeft, resRight = left, right
                left, right = left - 1, right + 1
            
            # Even length
            left, right = i, i + 1
            while left >= 0 and right < N and s[left] == s[right]:
                if right - left + 1 > resRight - resLeft + 1:
                    resLeft, resRight = left, right
                left, right = left - 1, right + 1
        return s[resLeft : resRight + 1]