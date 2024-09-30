"""
Accepted
50 [Medium]
Runtime: 40 ms, faster than 20.77% of Python3 online submissions for Pow(x, n).
Memory Usage: 16.76 MB, less than 18.35% of Python3 online submissions for Pow(x, n).
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(prod, n):
            if n == 0:
                return 1
            half = rec(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
                
        if n < 0:
            return 1 / rec(x, abs(n))
        else:
            return rec(x, n)