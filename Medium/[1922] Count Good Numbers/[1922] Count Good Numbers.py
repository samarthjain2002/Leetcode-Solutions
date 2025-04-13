"""
Accepted
1922 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Count Good Numbers.
Memory Usage: 17.70 MB, less than 93.38% of Python3 online submissions for Count Good Numbers.
"""
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even = ceil(n / 2)
        odd = n // 2

        def pow(x, n):
            res = 1
            while n > 0:
                if n % 2:
                    res = (res * x) % MOD
                n = n // 2
                x = (x * x) % MOD
            return res

        return (pow(5, even) * pow(4, odd)) % MOD