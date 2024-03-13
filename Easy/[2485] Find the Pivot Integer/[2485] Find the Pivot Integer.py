"""
Accepted
2485 [Easy]
Runtime: 70 ms, faster than 29.35% of Python3 online submissions for Find the Pivot Integer.
Memory Usage: 16.6 MB, less than 23.99% of Python3 online submissions for Find the Pivot Integer.
"""
class Solution:
    def pivotInteger(self, n: int) -> int:
        def summ(num):
            if num % 2 == 0:
                return (num + 1) * (num / 2)
            else:
                return ((num + 1) * (num // 2)) + ((num + 1) / 2)

        for i in range(n // 2, n + 1):
            if summ(i) == summ(n) - summ(i - 1):
                return i

        return -1