"""
Accepted
32 [Hard]
Runtime: 9 ms, faster than 22.71% of Python3 online submissions for Longest Valid Parentheses.
Memory Usage: 17.81 MB, less than 57.90% of Python3 online submissions for Longest Valid Parentheses.
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = 0
        res = 0
        for par in s:
            if par == '(':
                left += 1
            elif par == ')':
                right += 1

            if left == right:
                res = max(res, left * 2)
            elif left < right:
                left = right = 0

        left = right = 0
        for par in s[::-1]:
            if par == '(':
                left += 1
            elif par == ')':
                right += 1

            if left == right:
                res = max(res, left * 2)
            elif left > right:
                left = right = 0

        return res