"""
Accepted
633 [Medium]
Runtime: 146 ms, faster than 17.86% of Python3 online submissions for Sum of Square Numbers.
Memory Usage:  20.59 MB, less than 5.56% of Python3 online submissions for Sum of Square Numbers.
"""
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squareroot = set()

        for i in range(int(sqrt(c)) + 1):
            squareroot.add(i * i)

        a = 0
        while a * a <= c:
            target = c - a * a
            if target in squareroot:
                return True
            a += 1
        return False