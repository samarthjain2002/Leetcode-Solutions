"""
Accepted
20 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Valid Parentheses.
Memory Usage: 18.04 MB, less than 9.96% of Python3 online submissions for Valid Parentheses.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        counterPart = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in ")]}":
                if not stack or stack[-1] != counterPart[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        return not stack