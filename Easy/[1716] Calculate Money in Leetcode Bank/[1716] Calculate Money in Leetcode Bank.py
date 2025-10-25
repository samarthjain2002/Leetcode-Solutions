"""
Accepted
1716 [Easy]
Runtime: 33 ms, faster than 91.19% of Python3 online submissions for Calculate Money in Leetcode Bank.
Memory Usage: 16.36 MB, less than 7.77% of Python3 online submissions for Calculate Money in Leetcode Bank.
"""
# Math approach
# TC: O(1), SC: O(1)
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        low = 28
        high = (weeks + 3) * 7
        savings = weeks * (low + high) // 2

        for i in range(n % 7):
            savings += weeks + 1 + i

        return savings



"""
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Calculate Money in Leetcode Bank.
Memory Usage: 17.80 MB, less than 60.62% of Python3 online submissions for Calculate Money in Leetcode Bank.
"""
# Simulation approach
# TC: O(n), SC: O(1)
class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0

        full_weeks = (n // 7)
        res = full_weeks * (((7 + 1) * 7) // 2)

        for i in range(1, full_weeks):
            res += i * 7
        
        n = n % 7
        for i in range(1, n + 1):
            res += i + full_weeks

        return res
