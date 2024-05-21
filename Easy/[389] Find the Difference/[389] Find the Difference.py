"""
Accepted
389 [Easy]
Runtime: 79 ms, faster than 83.15% of Python3 online submissions for Find the Difference.
Memory Usage: 16.71 MB, less than 66.48% of Python3 online submissions for Find the Difference.
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