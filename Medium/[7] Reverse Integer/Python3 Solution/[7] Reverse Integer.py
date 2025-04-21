"""
Accepted
7 [Medium]
Runtime: 50 ms, faster than 7.29% of Python3 online submissions for Reverse Integer.
Memory Usage: 17.82 MB, less than 36.88% of Python3 online submissions for Reverse Integer.
"""
class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        x = abs(x)

        if x == 0:
            return 0
        exp = int(math.log10(x))

        res = 0
        while x:
            res += (x % 10) * 10**exp
            x = x // 10
            exp -= 1
        res = -1 * res if neg else res
        
        return 0 if res > 2**31 - 1 or res < -2**31 else res



"""
Runtime: 41 ms, faster than 43.52% of Python3 online submissions for Reverse Integer.
Memory Usage: 17.71 MB, less than 57.29% of Python3 online submissions for Reverse Integer.
"""
class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        s = str(x)[1 : ] if neg else str(x)
        s = s[::-1]
        rev = -1 * int(s) if neg else int(s)
        return 0 if rev > 2**31 - 1 or rev < -2**31 else rev