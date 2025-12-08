"""
Accepted
1925 [Easy]
Runtime: 225 ms, faster than 47.01% of Python online submissions for Count Square Sum Triples.
Memory Usage: 17.63 MB, less than 80.71% of Python online submissions for Count Square Sum Triples.
"""
class Solution:
    def countTriples(self, n: int) -> int:
        s = set([i*i for i in range(1, n + 1)])
        res = 0
        for i in range(1, 250):
            for j in range(i + 1, 250):
                a, b = i**2, j**2
                if a + b in s:
                    res += 2
        return res