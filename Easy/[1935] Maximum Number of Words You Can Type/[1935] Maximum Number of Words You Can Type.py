"""
Accepted
1935 [Easy]
Runtime: 161 ms, faster than 32.72% of Python online submissions for Maximum Number of Words You Can Type.
Memory Usage: 17.88 MB, less than 57.65% of Python online submissions for Maximum Number of Words You Can Type.
"""
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        res = len(words)
        for word in words:
            for char in word:
                if char in brokenLetters:
                    res -= 1
                    break
        return res