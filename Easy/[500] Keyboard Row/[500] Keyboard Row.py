"""
Accepted
500 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Keyboard Row.
Memory Usage: 17.90 MB, less than 30.62% of Python3 online submissions for Keyboard Row.
"""
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rowNumber = {}
        for char in "qwertyuiop":
            rowNumber[char] = 1
        for char in "asdfghjkl":
            rowNumber[char] = 2
        for char in "zxcvbnm":
            rowNumber[char] = 3

        res = []
        for word in words:
            row = rowNumber[word[0].lower()]
            for char in word:
                if rowNumber[char.lower()] != row:
                    break
            else:
                res.append(word)
        return res