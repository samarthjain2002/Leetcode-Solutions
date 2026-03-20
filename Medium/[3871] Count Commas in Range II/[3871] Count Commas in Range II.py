"""
Accepted
3871 [Medium]
Runtime: 1 ms, faster than 25.69% of Python3 online submissions for Count Commas in Range II.
Memory Usage: 19.29 MB less than 58.54% of Python3 online submissions for Count Commas in Range II.
"""
class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        for i in range(15, 0, -3):
            res += max(0, (n - 10**i + 1) * ((len(str(n)) - 1) // 3))
            if res:
                n = 10**i - 1
        return res