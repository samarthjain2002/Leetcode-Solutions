"""
Accepted
438 [Medium]
Runtime: 19 ms, faster than 99.29% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 18.40 MB, less than 36.72% of Python3 online submissions for Find All Anagrams in a String.
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        sLen, pLen = len(s), len(p)
        pChars = [0] * 26
        for char in p:
            pChars[ord(char) - 97] += 1

        sChars = [0] * 26
        for i in range(pLen):
            sChars[ord(s[i]) - 97] += 1

        res = []
        if pChars == sChars:
            res.append(0)

        for i in range(pLen, sLen):
            sChars[ord(s[i]) - 97] += 1
            sChars[ord(s[i - pLen]) - 97] -= 1
            if pChars == sChars:
                res.append(i - pLen + 1)

        return res           