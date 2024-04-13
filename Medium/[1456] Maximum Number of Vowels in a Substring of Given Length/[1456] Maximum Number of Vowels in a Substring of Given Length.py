"""
Accepted
1456 [Medium]
Runtime: 113 ms, faster than 71.81% of Python online submissions for Maximum Number of Vowels in a Substring of Given Length.
Memory Usage: 17.36 MB, less than 28.40% of Python online submissions for Maximum Number of Vowels in a Substring of Given Length.
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        N = len(s)
        vowels = {'a','e','i','o','u'}
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1

        res = count
        for i in range(1, N - k + 1):
            if s[i - 1] in vowels:
                count -= 1
            if s[i + k - 1] in vowels:
                count += 1
            res = max(res, count)

        return res