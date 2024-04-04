"""
Accepted
1614 [Easy]
Runtime: 34 ms, faster than 66.43% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
Memory Usage: 16.51 MB, less than 38.30% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
"""
class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                res = max(res, count)
                count -= 1
        return res