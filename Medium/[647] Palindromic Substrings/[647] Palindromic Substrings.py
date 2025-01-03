"""
Accepted
647 [Medium]
Runtime: 77 ms, faster than 79.83% of Python3 online submissions for Palindromic Substrings.
Memory Usage:  16.56 MB, less than 72.69% of Python3 online submissions for Palindromic Substrings.
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0

        for i in range(N):
            # Odd length
            left = right = i
            while left >= 0 and right < N and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

            # Even length
            left, right = i, i + 1
            while left >= 0 and right < N and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1    

        return res