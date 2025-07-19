"""
Accepted
1190 [Medium]
Runtime: 33 ms, faster than 77.83% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.
Memory Usage: 16.68 MB, less than 13.14% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.
"""
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                stack = stack + temp
            else:
                stack.append(char)

        res = ""
        for char in stack:
            res += char
        return res