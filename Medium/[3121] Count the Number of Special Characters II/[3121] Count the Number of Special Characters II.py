"""
Accepted
3121 [Medium]
Runtime: 268 ms, faster than 52.94% of Python3 online submissions for Count the Number of Special Characters II.
Memory Usage: 21.74 MB, less than 52.88% of Python3 online submissions for Count the Number of Special Characters II.
"""
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        higher = {}
        for i, char in enumerate(word):
            if ord('A') <= ord(char) <= ord('Z'):
                if char not in higher:
                    higher[char] = i
            else:
                lower[char] = i

        res = 0
        for char in string.ascii_lowercase:
            if char in lower and chr(ord(char) - (ord('a') - ord('A'))) in higher:
                if lower[char] < higher[chr(ord(char) - (ord('a') - ord('A')))]:
                    res += 1
        return res