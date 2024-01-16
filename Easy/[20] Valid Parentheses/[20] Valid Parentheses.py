"""
Accepted
20 [Easy]
Runtime: 34 ms, faster than 82.22% of Python3 online submissions for Valid Parentheses.
Memory Usage:  17.55 MB, less than 9.12% of Python3 online submissions for Valid Parentheses.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            else:
                if char in hashMap and stack[-1] == hashMap[char]:
                    stack.pop()
                else:
                    stack.append(char)

        if stack:
            return False
        else:
            return True