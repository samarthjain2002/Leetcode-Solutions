"""
Accepted
3133 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Minimum Array End.
Memory Usage: 16.54 MB, less than 69.70% of Python3 online submissions for Minimum Array End.
"""
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # O(logn) solution
        res = x
        i_n = i_x = 1

        while i_n <= n - 1:
            if i_x & x == 0:
                if i_n & (n - 1):
                    res = res | i_x
                i_n = i_n << 1
            i_x = i_x << 1
        return res
        


        # O(n) solution
        res = x
        for i in range(n - 1):
            res += 1
            res = res | x
        return res