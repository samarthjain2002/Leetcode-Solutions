"""
Accepted
2000 [Easy]
Runtime: 34 ms, faster than 63.06% of Python3 online submissions for Reverse Prefix of Word.
Memory Usage: 16.68 MB, less than 9.30% of Python3 online submissions for Reverse Prefix of Word.
"""
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, char in enumerate(word):
            if char == ch:
                word1 = word[ : i + 1]
                return word1[::-1] + word[i + 1 : ]
        return word