"""
Accepted
1624 [Easy]
Runtime: 84 ms, faster than 5.12% of Python3 online submissions for Largest Substring Between Two Equal Characters
Memory Usage: 17.36 MB, less than 5.61% of Python3 online submissions for Largest Substring Between Two Equal Characters.
"""
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        firstOcc = {}
        for index in range(len(s)):
            if s[index] not in firstOcc:
                firstOcc[s[index]] = index
            else:
                res = max(res, index - firstOcc[s[index]] - 1)
        return res