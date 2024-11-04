"""
Accepted
3163 [Medium]
Runtime: 137 ms, faster than 90.07% of Python3 online submissions for String Compression III.
Memory Usage: 18.90 MB, less than 93.12% of Python3 online submissions for String Compression III.
"""
class Solution:
    def compressedString(self, word: str) -> str:
        N = len(word)
        curChar = word[0]
        freq = 1

        res = ""
        for i in range(1, N):
            if word[i] == curChar:
                freq += 1
            else:
                while freq > 9:
                    res += '9' + curChar
                    freq -= 9
                res += str(freq) + curChar

                curChar = word[i]
                freq = 1
        while freq > 9:
            res += '9' + curChar
            freq -= 9
        res += str(freq) + curChar

        return res