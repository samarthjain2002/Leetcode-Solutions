"""
Accepted
3120 [Easy]
Runtime: 3 ms, faster than 37.34% of Python3 online submissions for Count the Number of Special Characters I.
Memory Usage: 19.30 MB, less than 25.31% of Python3 online submissions for Count the Number of Special Characters I.
"""
# One-pass Solution
# TC: O(n), SC: O(n)
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        hashSet = set()
        for char in word:
            if ord('a') <= ord(char) <= ord('z'):
                if chr(ord(char) - (ord('a') - ord('A'))) in hashSet and char not in hashSet:
                    res += 1
            else:
                if chr(ord(char) + (ord('a') - ord('A'))) in hashSet and char not in hashSet:
                    res += 1
            hashSet.add(char)
        return res



"""
Runtime: 2 ms, faster than 42.11% of Python3 online submissions for Count the Number of Special Characters I.
Memory Usage: 19.21 MB, less than 64.16% of Python3 online submissions for Count the Number of Special Characters I.
"""
# Two-pass Solution
# TC: O(n), SC: O(n)
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        for char in word:
            if ord('a') <= ord(char) <= ord('z'):
                lower.add(char)

        higher = set()
        res = 0
        for char in word:
            if char not in higher and chr(ord(char) + (ord('a') - ord('A'))) in lower:
                higher.add(char)
                res += 1
        return res