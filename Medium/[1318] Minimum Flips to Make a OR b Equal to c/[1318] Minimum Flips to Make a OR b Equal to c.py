"""
Accepted
1318 [Medium]
Runtime: 34 ms, faster than 72.09% of Python3 online submissions for Minimum Flips to Make a OR b Equal to c.
Memory Usage: 17.67 MB, less than 39.78% of Python3 online submissions for Minimum Flips to Make a OR b Equal to c.
"""
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        for i in range(30):
            if not (c & (1 << i)):
                if a & (1 << i):
                    res += 1
                if b & (1 << i):
                    res += 1
            elif (not (a & (1 << i))) and (not (b & (1 << i))):
                res += 1
        return res