"""
Accepted
76 [Hard]
Runtime: 114 ms, faster than 55.26% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 17.37 MB, less than 63.60% of Python3 online submissions for Minimum Window Substring.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N = len(s)

        tDict = defaultdict(int)
        for char in t:
            tDict[char] += 1
        count = len(tDict)
            
        left, right = 0, 0
        length = float("inf")
        res = ""

        while right < N:
            if s[right] in tDict:
                tDict[s[right]] -= 1
                if tDict[s[right]] == 0:
                    count -= 1
            right += 1
            
            while count == 0:
                if right - left < length:
                    length = right - left
                    res = s[left: right]
                    if res == t:
                        return res
                if s[left] in tDict:
                    tDict[s[left]] += 1
                    if tDict[s[left]] > 0:
                        count += 1
                left += 1

        return res