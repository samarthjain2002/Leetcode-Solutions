"""
Accepted
22 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Generate Parentheses.
Memory Usage: 17.62 MB, less than 5.46% of Python3 online submissions for Generate Parentheses.
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def recursion(n, left, right, string):
            if len(string) == n * 2:
                res.append(string)
                return

            if right < left:
                recursion(n, left, right + 1, string + ')')
            if left < n:
                recursion(n, left + 1, right, string + '(')

        recursion(n, 0, 0, "")
        return res