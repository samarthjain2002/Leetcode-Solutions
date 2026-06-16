"""
Accepted
3612 [Medium]
Runtime: 27 ms, faster than 68.42% of Python3 online submissions for Process String with Special Operations I.
Memory Usage: 25.82 MB, less than 54.61% of Python3 online submissions for Process String with Special Operations I.
"""
class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for char in s:
            if char == '*':
                if res:
                    res.pop()
            elif char == '#':
                res += res
            elif char == '%':
                res = res[::-1]
            else:
                res += char
        return "".join(res)