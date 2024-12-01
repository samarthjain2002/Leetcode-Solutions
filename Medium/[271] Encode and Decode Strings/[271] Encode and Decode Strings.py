"""
Accepted
271 [Medium]
Runtime: 173 ms, faster than 48.26% of Python3 online submissions for Encode and Decode Strings.
Memory Usage:  24.83 MB, less than 30.52% of Python3 online submissions for Encode and Decode Strings.
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + '#' + s
        return string

    def decode(self, s: str) -> List[str]:
        N = len(s)
        i = 0
        res = []
        while i < N:
            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1
            length = int(length)
    
            word = ""
            for j in range(i + 1, i + 1 + length):
                word += s[j]
            res.append(word)
            word = ""

            i += length + 1
        return res