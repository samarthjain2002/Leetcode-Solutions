"""
Accepted
389 [Easy]
Runtime: 27 ms, faster than 97.43% of Python3 online submissions for Find the Difference.
Memory Usage: 16.56 MB, less than 85.07% of Python3 online submissions for Find the Difference.
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sDict = defaultdict(int)
        tDict = defaultdict(int)
        for c in s:
            sDict[c] += 1
        for c in t:
            tDict[c] += 1
        for key, val in tDict.items():
            if sDict[key] != val:
                return key