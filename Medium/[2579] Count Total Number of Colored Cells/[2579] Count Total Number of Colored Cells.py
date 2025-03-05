"""
Accepted
2579 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Count Total Number of Colored Cells.
Memory Usage: 17.57 MB, less than 94.74% of Python3 online submissions for Count Total Number of Colored Cells.
"""
# TC: O(1)
# SC: O(1)
class Solution:
    def coloredCells(self, n: int) -> int:
        return (2 * (n - 1) * n) + 1



"""
Runtime: 119 ms, faster than 33.08% of Python3 online submissions for Count Total Number of Colored Cells.
Memory Usage: 17.59 MB, less than 94.74% of Python3 online submissions for Count Total Number of Colored Cells.
"""
# TC: O(n)
# SC: O(1)
class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1
        for i in range(1, n):
            res += 4 * i
        return res