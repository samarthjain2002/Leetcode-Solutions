"""
Accepted
242 [Easy]
Runtime: 54 ms, faster than 58.18% of Java online submissions for Valid Anagram.
Memory Usage: 16.76 MB, less than 75.11% of Java online submissions for Valid Anagram.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        sDict = {}
        for char in s:
            if char not in sDict:
                sDict[char] = 0
            sDict[char] += 1

        tDict = {}
        for char in t:
            if char not in tDict:
                tDict[char] = 0
            tDict[char] += 1

        for char in sDict:
            if char not in tDict:
                return False
            if sDict[char] != tDict[char]:
                return False
        
        return True