"""
Accepted
3870 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Count Commas in Range.
Memory Usage: 19.13 MB less than 87.22% of Python3 online submissions for Count Commas in Range.
"""
class Solution:
    def countCommas(self, n: int) -> int:
        return max(0, n - 1000 + 1)