"""
Accepted
1716 [Easy]
Runtime: 33 ms, faster than 91.19% of Python3 online submissions for Calculate Money in Leetcode Bank.
Memory Usage: 16.36 MB, less than 7.77% of Python3 online submissions for Calculate Money in Leetcode Bank.
"""
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        low = 28
        high = (weeks + 3) * 7
        savings = weeks * (low + high) // 2

        for i in range(n % 7):
            savings += weeks + 1 + i

        return savings