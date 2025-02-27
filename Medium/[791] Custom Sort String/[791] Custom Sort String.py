"""
Accepted
791 [Medium]
Runtime: 34 ms, faster than 68.03% of Python3 online submissions for Custom Sort String.
Memory Usage: 16.48 MB, less than 91.57% of Python3 online submissions for Custom Sort String.
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freqDict = defaultdict(int)
        for char in s:
            freqDict[char] += 1

        s = ""
        for char in order:
            s += char * freqDict[char]
            freqDict[char] = 0

        for key, val in freqDict.items():
            s += key * val

        return s