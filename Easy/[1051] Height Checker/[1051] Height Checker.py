"""
Accepted
1051 [Easy]
Runtime: 45 ms, faster than 17.28% of Python3 online submissions for Height Checker.
Memory Usage: 16.49 MB, less than 53.11% of Python3 online submissions for Height Checker.
"""
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        expected.sort()
        res = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                res += 1
        return res