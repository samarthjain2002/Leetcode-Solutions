"""
Accepted
1347 [Medium]
Runtime: 155 ms, faster than 62.81% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
Memory Usage:  17.81 MB, less than 21.41% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
"""
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sDict = defaultdict(int)
        tDict = defaultdict(int)
        for i in range(len(s)):
            sDict[s[i]] += 1
            tDict[t[i]] += 1
            
        count = 0
        for key, value in sDict.items():
            if tDict[key] >= value:
                print(key)
                count += value
            else:
                count += tDict[key]
            
        return len(s) - count